def calculate_score(value, risk):
    return value - risk

score = calculate_score(9, 3)
print("Decision score:", score)

if score >= 5:
    print("Recommendation: Proceed")
else:
    print("Recommendation: Review first")
