import json

raw_json = """
{
  "title": "Automate VAF decision summaries",
  "business_value": 8,
  "risk": 4,
  "readiness": 7
}
"""

model = json.loads(raw_json)
print("Title:", model["title"])
print("Readiness:", model["readiness"])
