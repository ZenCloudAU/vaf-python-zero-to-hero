from pathlib import Path

decision = {
    "title": "Publish Python Zero to Hero",
    "score": 21,
    "recommendation": "Strong candidate",
}

markdown = f"""# Decision Summary

## Title
{decision['title']}

## Score
{decision['score']}

## Recommendation
{decision['recommendation']}
"""

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)
path = output_dir / "vaf_decision_summary.md"
path.write_text(markdown, encoding="utf-8")
print("Generated:", path)
