import os
from dotenv import load_dotenv
from groq import Groq
from prompts import QUESTION_BANK, SYSTEM_PROMPT

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def call_llm(messages, model="llama-3.3-70b-versatile"):
    try:
        resp = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.6,
            max_tokens=800
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"[LLM error: {e}]"

class InterviewEngine:
    def __init__(self, role="software_engineer", max_questions=5):
        self.role = role
        self.max_questions = max_questions
        self.questions = QUESTION_BANK.get(role, [])
        self.history = []  # list of dicts {q, answer, followups}

    def pick_question(self, idx):
        if idx < len(self.questions):
            return self.questions[idx]
        else:
            return "Tell me about a time you faced a difficult problem and how you resolved it."

    def ask_question(self, q_text):
        print("\nINTERVIEWER:", q_text)
        ans = input("YOU: ").strip()
        return ans

    def need_followup(self, q_text, ans_text):
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Question: {q_text}\nAnswer: {ans_text}\nDo you need a follow-up? If yes, give a single concise follow-up question. If no, reply 'NO'."}
        ]
        resp = call_llm(messages)
        if resp.strip().upper() == "NO":
            return None
        return resp.strip()

    def evaluate(self):
        convo = ""
        for i, h in enumerate(self.history, start=1):
            convo += f"Q{i}: {h['q']}\nA{i}: {h['answer']}\n"
            for fu in h.get("followups", []):
                convo += f"Followup: {fu}\n"
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Provide post-interview feedback on the following exchange:\n{convo}\nGive the feedback in sections: Communication (1-5), Content/Technical (1-5), Strengths, Improvements (3 concrete advice)."}
        ]
        feedback = call_llm(messages)
        return feedback

    def run(self):
        print(f"Starting mock interview for role: {self.role}\nType 'END' anytime to finish and get feedback.\n")
        idx = 0
        while idx < self.max_questions:
            q = self.pick_question(idx)
            ans = self.ask_question(q)
            if ans.strip().upper() == "END":
                break
            record = {"q": q, "answer": ans, "followups": []}
            fu = self.need_followup(q, ans)
            if fu:
                print("\nINTERVIEWER (follow-up):", fu)
                fu_ans = input("YOU: ").strip()
                if fu_ans.upper() == "END":
                    break
                record["followups"].append(fu + " || Answer: " + fu_ans)
            self.history.append(record)
            idx += 1

        print("\n--- Interview finished. Generating feedback... ---\n")
        feedback = self.evaluate()
        print("\nFEEDBACK:\n")
        print(feedback)
        print("\n--- End ---")
