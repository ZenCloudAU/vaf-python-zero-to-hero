request = {
    "method": "POST",
    "path": "/vaf/decision-score",
    "body": {"value": 9, "risk": 3, "confidence": 7},
}

body = request["body"]
response = {
    "status": 200,
    "score": body["value"] + body["confidence"] - body["risk"],
}

print("Request:", request)
print("Response:", response)
