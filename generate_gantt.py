import csv
from datetime import datetime

INPUT_FILE = "../data/conferences_2026_2027.csv"
OUTPUT_FILE = "../generated_gantt.md"

def days_between(start, end):
    d1 = datetime.strptime(start, "%Y-%m-%d")
    d2 = datetime.strptime(end, "%Y-%m-%d")
    return (d2 - d1).days

sections = {}

with open(INPUT_FILE, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        area = row["area"]
        name = row["conference"]
        round_ = row["round"]
        submission = row["submission"]
        final = row["final_notification"]

        duration = days_between(submission, final)

        label = f"{name} '{round_}"
        entry = f"    {label} :{name.lower()}{round_.lower()}, {submission}, {duration}d"

        sections.setdefault(area, []).append(entry)

with open(OUTPUT_FILE, "w") as f:
    f.write("```mermaid\n")
    f.write("gantt\n")
    f.write("    dateFormat YYYY-MM-DD\n")
    f.write("    title Submission & Review Timelines (2026–2027)\n\n")

    for area, entries in sections.items():
        f.write(f"    section {area}\n")
        for e in entries:
            f.write(e + "\n")
        f.write("\n")

    f.write("```\n")

print("Mermaid Gantt generated -> generated_gantt.md")
