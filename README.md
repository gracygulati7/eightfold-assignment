# Interview Practice Partner (AI Mock Interview Agent)

This project is an **AI-powered mock interview assistant** built for the **“AI Agent Building Assignment – Eightfold AI”**

The agent supports multiple interview roles, asks dynamic follow-up questions, evaluates answers, and gives structured feedback — all powered by **Groq’s free LLaMA 3.3 70B model**, so **no paid credits or API charges** are required.

---

## Demo Video

Click below to watch the full demo:

[Demo Video](eightfold_demo_video.mp4)

## Features

### Multi-role Interviewer

Choose from:

* Software Engineer
* Sales
* Retail Associate

Each role has a unique question bank.

### Dynamic Follow-up Questions

After each user answer:

* The AI analyzes it
* Decides if a follow-up is needed
* Generates a focused follow-up question

### Evaluation & Feedback

At the end, the AI provides:

* Communication score
* Content score
* Strengths
* Weaknesses
* Actionable improvement steps

### Free to run (Groq API)

The assistant uses:
**Groq’s LLaMA-3.3-70B-Versatile** model
— completely free, extremely fast, and no credit card required.

---

## Getting Started

### 1️⃣ **Clone the repository**

```bash
git clone https://github.com/gracygulati7/eightfold-assignment
cd eightfold-assignment
```

---

### 2️⃣ **Create & activate virtual environment**

#### Windows (PowerShell)

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

---

### 3️⃣ **Install dependencies**

Make sure you are inside your virtual environment:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ **Set up your `.env` file**

Create a file named `.env` in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

#### Where to get your API key:

1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Log in → Left sidebar → **API Keys**
3. Create a key and paste it into `.env`

✔️ Groq is **free**
✔️ No credit card required
✔️ This project uses the key for all AI calls

---

## Running the Interview Assistant

Inside the virtual environment:

```bash
python run.py
```

### Example flow:

```
Choose a role:
1. Software Engineer
2. Sales
3. Retail Associate

INTERVIEWER: Tell me about a time you designed a scalable system...
YOU: I'm a fresher but I can explain how I would approach it.

INTERVIEWER (follow-up): What design trade-offs would you consider?
YOU: <your answer>

--- Feedback will be generated at the end ---
```

Type **END** anytime to stop the interview early.

---

## Project Structure

```
├── prompts.py               # Static question bank + system prompts
├── interview_engine.py      # Main logic: follow-ups, evaluation, LLM calls
├── run.py                   # CLI interface
├── requirements.txt         # Dependencies
├── .env.example             # Template env file (no key)
└── README.md                # Documentation
```

---

## Tech Stack

| Component      | Technology                         |
| -------------- | ---------------------------------- |
| LLM Provider   | **Groq (LLaMA-3.3-70B-Versatile)** |
| Language       | Python 3.10+                       |
| Env Management | Python `venv`                      |
| API Client     | `groq` Python SDK                  |
| Config         | `.env` via `python-dotenv`         |

---

### ✔️ Show robust behavior

* Model responds even to weak answers
* Follow-ups appear
* Final feedback is well structured

---

LLaMA documentation (Groq):
➡️ [https://console.groq.com/docs](https://console.groq.com/docs)

---

## Acknowledgements

Special thanks to **Groq** for offering free access to cutting-edge LLaMA models, enabling students to build powerful AI applications without paid credits.

---

## License

This project is for educational and personal use as part of the Eightfold AI Agent Building Assignment. You may extend or modify it freely.
