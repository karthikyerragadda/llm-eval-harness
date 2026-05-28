import streamlit as st
import pandas as pd
import plotly.express as px
from evaluator import run_evaluation

# Page config
st.set_page_config(page_title="LLM Eval Harness", page_icon="🧪", layout="wide")
st.title("🧪 LLM Evaluation Harness")
st.caption("Evaluating Claude's performance on legal document Q&A")

# Sidebar
st.sidebar.title("About")
st.sidebar.write("""
This harness evaluates Claude across 10 legal Q&A questions using 3 scoring methods:
- **Exact Match** — does the answer contain the expected phrase?
- **Keyword Score** — how many expected keywords appear?
- **Judge Score** — Claude rates its own answer out of 10
""")

# Run evaluation button
if st.button("▶ Run Evaluation", type="primary"):
    with st.spinner("Running 10 evaluations... this will take about 30 seconds"):
        results = run_evaluation()
        df = pd.DataFrame(results)
        st.session_state.results = df
        st.session_state.ran = True

# Display results
if "ran" in st.session_state and st.session_state.ran:
    df = st.session_state.results

    # ── Top metrics ──────────────────────────────────────────────────────────
    st.subheader("📊 Overall Performance")
    col1, col2, col3, col4 = st.columns(4)

    total = len(df)
    passes = df["Exact Match"].str.contains("Pass").sum()
    avg_keyword = round(df["Keyword Score (%)"].mean())
    avg_judge = round(df["Judge Score (/10)"].mean(), 1)

    col1.metric("Exact Match Rate", f"{passes}/{total}", f"{round(passes/total*100)}%")
    col2.metric("Avg Keyword Score", f"{avg_keyword}%")
    col3.metric("Avg Judge Score", f"{avg_judge}/10")
    col4.metric("Questions Evaluated", total)

    # ── Charts ───────────────────────────────────────────────────────────────
    st.subheader("📈 Score Breakdown")
    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.bar(
            df, x="ID", y="Keyword Score (%)",
            title="Keyword Score per Question",
            color="Keyword Score (%)",
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.bar(
            df, x="ID", y="Judge Score (/10)",
            title="Judge Score per Question",
            color="Judge Score (/10)",
            color_continuous_scale="Greens"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # ── Results table ─────────────────────────────────────────────────────────
    st.subheader("📋 Detailed Results")
    st.dataframe(
        df[["ID", "Question", "Expected", "Exact Match", 
            "Keyword Score (%)", "Judge Score (/10)", "Overall Score (%)"]],
        use_container_width=True
    )

    # ── Individual responses ──────────────────────────────────────────────────
    st.subheader("💬 Individual Responses")
    for _, row in df.iterrows():
        with st.expander(f"Q{row['ID']}: {row['Question']} — {row['Exact Match']}"):
            col1, col2 = st.columns(2)
            col1.write(f"**Expected:** {row['Expected']}")
            col1.write(f"**Keyword Score:** {row['Keyword Score (%)']}%")
            col1.write(f"**Judge Score:** {row['Judge Score (/10)']}/10")
            col2.write(f"**Claude's Response:**")
            col2.write(row["Response"])

else:
    st.info("👆 Click 'Run Evaluation' to start testing Claude on 10 legal questions!") 
