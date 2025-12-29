# Autonomous CI/CD Intelligence Agent

An AI-powered CI/CD decision engine that evaluates code changes using
semantic RAG and historical incident knowledge to recommend deployment actions.

## Features
- CI/CD event listener (FastAPI)
- LangChain-style agent reasoning
- Semantic RAG using FAISS + HuggingFace embeddings
- Deployment risk analysis with explanations

## Architecture
CI/CD Event → RAG (Vector DB) → LLM Agent → Deployment Decision

## Example Input
```json
{
  "commit_message": "Updated auth middleware",
  "tests": "passed",
  "files_changed": ["auth.py"]
}
Example Output
json
Copy code
{
  "risk": "HIGH",
  "recommendation": "Run additional tests or block deployment"
}
```
## Tech Stack
Python

FastAPI

LangChain

FAISS

HuggingFace Embeddings