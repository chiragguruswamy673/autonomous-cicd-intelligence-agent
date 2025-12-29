def analyze_change(payload: dict, similar_incidents: list):
    commit = payload.get("commit_message", "").lower()

    if "auth" in commit:
        return {
            "risk": "HIGH",
            "reason": "Authentication related change detected",
            "recommendation": "Run additional tests or block deployment"
        }

    return {
        "risk": "LOW",
        "reason": "No risky patterns detected",
        "recommendation": "Allow deployment"
        }
