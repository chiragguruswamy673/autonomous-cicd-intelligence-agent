from fastapi import FastAPI
from app.decision_engine import evaluate_deployment

app = FastAPI()   # 👈 THIS MUST EXIST

@app.post("/cicd-event")
def cicd_event(payload: dict):
    return evaluate_deployment(payload)
