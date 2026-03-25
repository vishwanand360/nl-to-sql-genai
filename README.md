# 🧠 Natural Language to SQL Query System (GenAI + AWS)

A secure **GenAI-powered application** that converts natural language queries into SQL using **Amazon Bedrock (Claude)** and executes them safely on a relational database.

---

## 🚀 Project Overview

This project allows users to ask questions in plain English such as:

> "Show all users"  
> "Get all records from database"

The system automatically:
- Converts natural language → SQL using LLM
- Validates SQL queries for safety
- Executes queries securely on database
- Displays results in real-time

---

## 🏗️ Architecture
User (Streamlit UI)
↓
FastAPI Backend (REST API)
↓
Amazon Bedrock (Claude LLM)
↓
SQL Validation Layer
↓
SQLite Database


---

## ✨ Features

- 🔹 Natural Language → SQL conversion using GenAI  
- 🔹 Schema-aware prompt engineering  
- 🔹 Secure SQL validation (SELECT-only enforcement)  
- 🔹 Protection against SQL injection  
- 🔹 Automatic row limiting for safe queries  
- 🔹 FastAPI backend with REST APIs  
- 🔹 Streamlit UI for interactive usage  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy  
- **Frontend:** Streamlit  
- **AI / GenAI:** Amazon Bedrock (Claude 3 Haiku)  
- **Database:** SQLite  
- **Cloud SDK:** boto3  
- **Validation:** Pydantic  

---

## 📁 Project Structure


nl_to_sql/
│
├── app.py # Streamlit UI
├── main.py # FastAPI backend
├── llm.py # Bedrock (Claude) integration
├── security.py # SQL validation layer
├── db.py # Database setup
├── requirements.txt
├── README.md
└── .gitignore


---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/vishwanand360/nl-to-sql-genai.git
cd nl-to-sql-genai
2️⃣ Create virtual environment
python -m venv venv

Activate (Windows CMD):

venv\Scripts\activate.bat
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure AWS
aws configure

Use:

Region: us-east-1
Enable Amazon Bedrock access
Attach AmazonBedrockFullAccess policy
5️⃣ Run Backend
uvicorn main:app --reload

Backend runs at:

http://127.0.0.1:8000
6️⃣ Run Frontend (New Terminal)
streamlit run app.py

Frontend runs at:

http://localhost:8501
🧪 Example Query

Input:

Show all users

Output:

Generated SQL query
Row count
Table results
🔐 Security Features
Only SELECT queries allowed
Dangerous SQL keywords blocked
Automatic LIMIT enforcement
LLM output sanitization before execution
🧠 Learning Outcomes
Practical use of Generative AI in backend systems
Hands-on experience with AWS Bedrock & IAM
Secure API development using FastAPI
Real-world debugging and system design
Full-stack integration (AI + Backend + UI)
📌 Future Improvements
Multi-database support (PostgreSQL, MySQL)
User authentication system
Query explanation in natural language
Cloud deployment (AWS EC2 / Docker)
👨‍💻 Author

Shubham
Aspiring Backend / GenAI Engineer

⭐ Support

If you like this project, give it a ⭐ and feel free to contribute!


---

# 🚀 WHAT TO DO NOW

1. Open your GitHub repo  
2. Click **README.md → Edit**  
3. **Paste this full content**  
4. Click **Commit changes**

---

# 🔥 AFTER THIS

Your repo becomes:
- ⭐ Professional  
- ⭐ Recruiter-ready  
- ⭐ Portfolio-level  

---

## 🚀 NEXT (VERY IMPORTANT)

Reply with:

1️⃣ **Add screenshots** 📸 (boosts impact a lot)  
2️⃣ **Add GitHub badges** 🏷  
3️⃣ **Deploy project online** 🌐  
4️⃣ **Interview Q&A** 🎯  

---

👉 You’re now building a **TOP-TIER portfolio** 🚀
