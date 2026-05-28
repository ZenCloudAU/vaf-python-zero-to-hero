from pathlib import Path
import runpy

ROOT = Path(__file__).parent
LESSONS = [
    "00_programming_refresher.py",
    "01_hello_python.py",
    "02_variables_values.py",
    "03_functions.py",
    "04_lists_dictionaries.py",
    "05_json_models.py",
    "06_files_and_folders.py",
    "07_csv_data.py",
    "08_api_basics.py",
    "09_decision_scoring_engine.py",
    "10_artefact_generator.py",
    "11_prompt_guardrails.py",
    "12_capstone_vaf_automation.py",
]

for lesson in LESSONS:
    path = ROOT / "src" / "lessons" / lesson
    print("\n" + "=" * 72)
    print(f"Running {lesson}")
    print("=" * 72)
    runpy.run_path(str(path), run_name="__main__")

print("\nAll Python lessons completed.")
