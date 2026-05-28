# LLM Evaluation Harness

A framework for evaluating Claude's performance on legal document Q&A 
using three scoring methods.

## Scoring Methods
- **Exact Match** — checks if the expected answer appears in the response
- **Keyword Score** — measures how many expected keywords appear (0-100%)
- **Claude-as-Judge** — Claude scores its own response out of 10

## Features
- 10 legal Q&A test cases with expected answers and keywords
- Interactive Streamlit dashboard with charts and metrics
- Per-question breakdown with pass/fail indicators
- Overall performance metrics at a glance

## Tech Stack
- Python
- Anthropic Claude API
- Streamlit
- Pandas
- Plotly

## Setup
1. Clone the repo
2. Create a virtual environment and install dependencies:
   pip install anthropic streamlit python-dotenv pandas plotly
3. Add your Anthropic API key to a .env file:
   ANTHROPIC_API_KEY=your_key_here
4. Run the app:
   streamlit run app.py 
