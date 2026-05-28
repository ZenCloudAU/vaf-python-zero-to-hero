import csv
from io import StringIO

csv_data = "title,value,risk\nAdopt Python,9,3\nGenerate reports,8,4\n"
reader = csv.DictReader(StringIO(csv_data))

for row in reader:
    score = int(row["value"]) - int(row["risk"])
    print(row["title"], "score:", score)
