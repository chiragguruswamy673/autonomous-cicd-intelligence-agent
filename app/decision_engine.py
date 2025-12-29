from app.agent import analyze_change
from app.rag import load_vector_db

def evaluate_deployment(payload: dict):
    try:
        db = load_vector_db()
        similar = db.similarity_search(
        payload.get("commit_message", ""),
        k=2
)

        decision = analyze_change(payload, similar)

        return {
            "deployment_decision": decision,
            "similar_incidents_found": [doc.page_content for doc in similar]
        }
    except Exception as e:
        return {
            "error": "Deployment evaluation failed",
            "details": str(e)
        }
