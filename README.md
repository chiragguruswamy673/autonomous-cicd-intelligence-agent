# 🚀 Autonomous CI/CD Intelligence Agent
![CI](https://github.com/chiragguruswamy673/autonomous-cicd-intelligence-agent/actions/workflows/ci.yml/badge.svg)
An AI-powered CI/CD decision system that analyzes code changes, retrieves
historical incidents using **semantic RAG**, and produces intelligent
deployment recommendations.

This project demonstrates how **GenAI can be embedded directly into
software delivery pipelines**, not just chatbots or Q&A systems.

---

## 🧠 What Problem Does This Solve?

Modern CI/CD pipelines rely on:
- Static rules
- Binary pass/fail signals
- Human judgment for risky deployments

This system introduces an **AI reasoning layer** that:
- Understands *what changed*
- Learns from *past failures*
- Assesses *deployment risk*
- Explains *why a deployment should proceed or be blocked*

---

## ✨ Key Features

- 🔌 **CI/CD Event Listener** (FastAPI)
- 🤖 **LLM-style Decision Agent**
- 🧠 **Semantic RAG (Retrieval-Augmented Generation)**
- 📚 **Vector Database (FAISS)**
- 🔍 **HuggingFace Embeddings**
- ⚙️ **Automated CI Pipeline (GitHub Actions)**
- 📈 **Production-style Architecture**

---

## 🏗️ High-Level Architecture

CI/CD Event (Commit, Tests, Files)
↓
FastAPI Endpoint
↓
Semantic RAG Engine
(FAISS + Embeddings)
↓
Decision Agent
↓
Deployment Recommendation

yaml
Copy code

---

## 📥 Example Input (CI/CD Event)

```json
{
  "commit_message": "Updated auth middleware",
  "tests": "passed",
  "files_changed": ["auth.py"]
}
```
## 📤 Example Output
```json
Copy code
{
  "deployment_decision": {
    "risk": "HIGH",
    "reason": "Authentication related change detected",
    "recommendation": "Run additional tests or block deployment"
  },
  "similar_incidents_found": [
    "Login deployment caused auth failures",
    "High memory usage after API release"
  ]
}
```
➡️ The system detects high-risk auth changes and retrieves
semantically similar past incidents — even without exact keyword matches.

## 🧪 How It Works (Step-by-Step)
A CI/CD event is sent to /cicd-event

The agent embeds the commit message

FAISS retrieves similar historical incidents

The decision engine reasons over:

Code change context

Test status

Past failures

A deployment recommendation is returned with explanation

## 🛠️ Tech Stack
Category	Technology
Backend	FastAPI
AI / RAG	LangChain-style architecture
Embeddings	HuggingFace sentence-transformers
Vector DB	FAISS
CI	GitHub Actions
Language	Python 3.11

## ▶️ Running Locally
1️⃣ Setup Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2️⃣ Start the Service
bash
Copy code
uvicorn app.main:app --reload
3️⃣ Open API Docs
arduino
Copy code
http://127.0.0.1:8000/docs
🔁 CI/CD Pipeline
This repository includes a GitHub Actions CI pipeline that:

Installs dependencies

Loads the FastAPI app

Executes an automated API smoke test

This ensures the CI/CD intelligence agent is validated on every push.

## 🎯 Why This Project Is Different
Most GenAI projects focus on:

Chatbots

PDF Q&A

Toy RAG demos

This project embeds AI reasoning directly into the software delivery
lifecycle, demonstrating:

System design thinking

Real-world CI/CD integration

Semantic retrieval over historical failures

Explainable AI decisions

## 🚀 Future Enhancements
Persist FAISS index to disk

Integrate real CI platforms (GitHub webhooks)

Add rollback automation

Replace mock logic with live LLM inference

Multi-service risk aggregation

## 👤 Author
Chirag Guruswamy