from pathlib import Path

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

path = output_dir / "lesson_06_output.txt"
path.write_text("Python can write generated architecture outputs.\n", encoding="utf-8")

print("Wrote:", path)
