from pathlib import Path

portfolio = [
    {"title": "Publish Python Zero to Hero", "business_value": 9, "risk": 3, "readiness": 8, "confidence": 7},
    {"title": "Automate artefact summaries", "business_value": 8, "risk": 4, "readiness": 7, "confidence": 6},
]

def score(item):
    return item["business_value"] + item["readiness"] + item["confidence"] - item["risk"]

lines = ["# VAF Automation Summary", ""]
for item in portfolio:
    item_score = score(item)
    recommendation = "Approve" if item_score >= 20 else "Review"
    lines.append(f"- {item['title']}: {item_score} ({recommendation})")

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
path = output_dir / "capstone_summary.md"
path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Generated:", path)
print("Capstone complete.")
