QUESTION_BANK = {
    "software_engineer": [
        "Tell me about a time you designed a system to handle high load. What choices did you make and why?",
        "How would you debug a production issue where latency suddenly increased 10x?",
        "Explain how you would design a URL shortening service. Discuss data model, API, and scaling."
    ],
    "sales": [
        "Walk me through how you qualify a new lead.",
        "Tell me about a time you lost a deal. What did you learn?",
        "How do you handle an objection about price?"
    ],
    "retail_associate": [
        "How do you handle a dissatisfied customer who wants a refund without a receipt?",
        "Describe a time you went above and beyond for a customer.",
        "How would you manage multiple customers during a busy shift?"
    ]
}

SYSTEM_PROMPT = """You are an interview assistant bot. Your job:
1) Ask the user role-specific interview questions (one at a time).
2) If the user's answer is brief or missing details, ask a focused follow-up question to get evidence.
3) After the interview (when user types 'END' or after N questions), provide structured feedback: Communication, Content/Technical, Strengths, Areas to improve, 2-3 concrete suggestions.
Be concise, actionable, and polite.
"""
