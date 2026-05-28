def score_decision(decision):
    return decision["business_value"] + decision["readiness"] + decision["confidence"] - decision["risk"]

def classify(score):
    if score >= 20:
        return "Strong candidate"
    if score >= 12:
        return "Needs review"
    return "Not ready"

decision = {"business_value": 9, "risk": 3, "readiness": 8, "confidence": 7}
score = score_decision(decision)
print("Score:", score)
print("Classification:", classify(score))
