# AI Job Interview Coach

An **AI-powered Job Interview Coach** built using **CrewAI**, **FastAPI**, and **Streamlit**.

This tool helps candidates prepare for interviews by generating real-time questions, evaluating responses, and providing constructive feedback.

---

## 🚀 Features

* **AI-generated interview questions** based on role/skills
* **Candidate response analysis**
* **Constructive feedback and improvement tips**
* **Interactive Streamlit frontend** + **FastAPI backend**

---

## 🛠️ Tech Stack

* **Python**
* **CrewAI**
* **FastAPI**
* **Streamlit**

---

## 📂 Project Setup

Follow these steps to get the project up and running locally:

### 1. Clone the repository

```bash
git clone https://github.com/Abdullahariff/AI-Job-Interview-Coach.git
cd ai-job-interview-coach

# It's recommended to use a virtual environment
# python -m venv venv
# source venv/bin/activate  # On Linux/macOS
# .\venv\Scripts\activate   # On Windows

pip install -r requirements.txt

OPENAI_API_KEY=your_key_here

uvicorn backend:app --reload

streamlit run frontend.py



📌 Usage
Select your job role and skillset.

Get AI-generated questions.

Type in your answers.

Receive instant feedback and improvement tips.

🤝 Contribution
Feel free to fork the repository, open issues, and submit PRs (Pull Requests).
