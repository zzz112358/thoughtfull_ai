# Thoughtful AI Support Agent

A simple **customer support AI agent** for Thoughtful AI, built with **Python** and **Streamlit**.
The agent answers common questions about Thoughtful AI’s automation agents using a **hardcoded knowledge base**, and falls back gracefully for unrecognized questions.

## Tech Stack

* **Python 3.10+**
* **Streamlit** – Web-based UI
* Standard library (`difflib` for string similarity)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/thoughtful-ai-agent.git
cd thoughtful-ai-agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

```bash
streamlit run app.py
```

Open the URL provided in your terminal (usually `http://localhost:8501`) to interact with the agent.

---

## How It Works

1. The agent receives a user question.
2. It compares the question with a **hardcoded knowledge base** using `difflib.SequenceMatcher`.
3. If the best match is above a **similarity threshold**, the corresponding answer is returned.
4. Otherwise, it fails back to openai call
---

## Future Improvements

* Replace string similarity with semantic embeddings for better matching
* Maintain chat history for context-aware responses
* Add automated tests for knowledge
