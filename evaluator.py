import anthropic
from dotenv import load_dotenv
from dataset import DATASET, CONTEXT

load_dotenv()

client = anthropic.Anthropic()

SYSTEM_PROMPT = """You are a legal document assistant. Answer questions 
based only on the contract provided. Be concise and specific."""


def get_response(question: str) -> str:
    """Send a question to Claude and get a response."""
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Contract:\n{CONTEXT}\n\nQuestion: {question}"
            }
        ]
    )
    return message.content[0].text


def exact_match_score(response: str, expected: str) -> bool:
    """
    Check if the expected answer appears in the response.
    Returns True (pass) or False (fail).
    """
    return expected.lower() in response.lower()


def keyword_score(response: str, keywords: list) -> float:
    """
    Check how many keywords appear in the response.
    Returns a score from 0 to 100.
    """
    response_lower = response.lower()
    found = [kw for kw in keywords if kw.lower() in response_lower]
    return round((len(found) / len(keywords)) * 100)


def claude_judge_score(question: str, response: str, expected: str) -> int:
    """
    Ask Claude to judge its own response.
    Returns a score from 0 to 10.
    """
    judge_prompt = f"""You are an evaluator. Score this answer from 0 to 10.

Question: {question}
Expected Answer: {expected}
Actual Response: {response}

Scoring criteria:
- 10: Perfect, contains the exact expected answer
- 7-9: Good, correct but could be more precise  
- 4-6: Partial, somewhat correct
- 1-3: Poor, mostly incorrect
- 0: Completely wrong or missing

Reply with ONLY a single number from 0 to 10. Nothing else."""

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=10,
        messages=[{"role": "user", "content": judge_prompt}]
    )
    
    try:
        return int(message.content[0].text.strip())
    except:
        return 0


def run_evaluation() -> list:
    """Run all evaluations and return results as a list of dicts."""
    results = []

    for item in DATASET:
        print(f"Evaluating question {item['id']}/10...")
        
        # Get Claude's response
        response = get_response(item["question"])

        # Score it three ways
        exact = exact_match_score(response, item["expected_answer"])
        keyword = keyword_score(response, item["keywords"])
        judge = claude_judge_score(item["question"], response, item["expected_answer"])

        results.append({
            "ID": item["id"],
            "Question": item["question"],
            "Expected": item["expected_answer"],
            "Response": response,
            "Exact Match": "✅ Pass" if exact else "❌ Fail",
            "Keyword Score (%)": keyword,
            "Judge Score (/10)": judge,
            "Overall Score (%)": round((keyword + judge * 10) / 2)
        })

    return results 
