def assess_prompt(request):
    if not request["context_provided"]:
        return "Add context before using AI."
    if not request["success_criteria"]:
        return "Define success criteria first."
    if request["risk_level"] == "high":
        return "Human review required."
    return "Prompt is ready to use."

request = {
    "task": "Generate a VAF artefact",
    "context_provided": True,
    "success_criteria": True,
    "risk_level": "medium",
}

print("Assessment:", assess_prompt(request))
