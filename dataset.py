# This is our evaluation dataset
# Each entry has:
# - question: what we ask Claude
# - expected_answer: the key phrase we expect in the response
# - keywords: words we expect to appear in the response
# - context: the legal text Claude should use to answer

CONTEXT = """
SERVICE AGREEMENT

This Service Agreement is entered into as of January 1, 2025, 
between ABC Company ("Client") and XYZ Consulting ("Service Provider").

1. SERVICES
Service Provider agrees to provide software development services to Client 
for a period of 12 months.

2. PAYMENT
Client agrees to pay Service Provider $5,000 per month, due on the 1st of 
each month. Late payments incur a 5% penalty after 10 days.

3. TERMINATION
Either party may terminate this agreement with 30 days written notice. 
Client must pay for all work completed up to termination date.

4. CONFIDENTIALITY
Service Provider agrees to keep all client information strictly confidential 
and not disclose to any third party.

5. LIABILITY
Service Provider's liability is limited to the total amount paid in the 
previous 3 months.
"""

DATASET = [
    {
        "id": 1,
        "question": "How much does the client pay per month?",
        "expected_answer": "$5,000",
        "keywords": ["5000", "month", "payment"]
    },
    {
        "id": 2,
        "question": "What is the penalty for late payment?",
        "expected_answer": "5%",
        "keywords": ["5%", "penalty", "late", "10 days"]
    },
    {
        "id": 3,
        "question": "How many days notice is required to terminate?",
        "expected_answer": "30 days",
        "keywords": ["30", "days", "notice", "terminate"]
    },
    {
        "id": 4,
        "question": "What type of services does the agreement cover?",
        "expected_answer": "software development",
        "keywords": ["software", "development", "services"]
    },
    {
        "id": 5,
        "question": "How long is the agreement for?",
        "expected_answer": "12 months",
        "keywords": ["12", "months", "period"]
    },
    {
        "id": 6,
        "question": "Who are the two parties in this agreement?",
        "expected_answer": "ABC Company",
        "keywords": ["ABC", "XYZ", "client", "service provider"]
    },
    {
        "id": 7,
        "question": "What is the liability limit for the service provider?",
        "expected_answer": "3 months",
        "keywords": ["liability", "limited", "3 months"]
    },
    {
        "id": 8,
        "question": "When is payment due each month?",
        "expected_answer": "1st of each month",
        "keywords": ["1st", "month", "due"]
    },
    {
        "id": 9,
        "question": "Can the client share the service provider's work with others?",
        "expected_answer": "No",
        "keywords": ["confidential", "not disclose", "third party"]
    },
    {
        "id": 10,
        "question": "What happens to payment if the agreement is terminated?",
        "expected_answer": "pay for all work completed",
        "keywords": ["pay", "work", "completed", "termination"]
    }
] 
