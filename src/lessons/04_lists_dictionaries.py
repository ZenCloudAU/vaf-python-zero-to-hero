decisions = [
    {"title": "Adopt Python", "value": 9, "risk": 3},
    {"title": "Generate artefacts", "value": 8, "risk": 4},
    {"title": "Skip review", "value": 2, "risk": 9},
]

for decision in decisions:
    score = decision["value"] - decision["risk"]
    print(decision["title"], "score:", score)
