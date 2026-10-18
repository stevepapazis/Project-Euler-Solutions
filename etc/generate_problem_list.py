from pathlib import Path
import re
import sys

from bs4 import BeautifulSoup

soup = BeautifulSoup(
    Path(sys.argv[1]).read_text(encoding="utf-8"),
    "html.parser"
)

heading = soup.find(
    string=lambda text: text and "Solved" in text and "out of" in text
)

match = re.search(r"Solved\s+(\d+)\s+out of\s+(\d+)", heading or "")

if not match:
    raise ValueError("Could not find solved-problem statistics in the HTML.")

solved = int(match.group(1))
total = int(match.group(2))
remaining = total - solved

ids = []
titles = []
dates = []

for row in soup.select("table tr"):
    number_cell = row.select_one("td.center")
    link = row.select_one("td a[href*='/problem=']")
    date_cell = row.select_one("td.monospace")

    if not all([number_cell, link, date_cell]):
        continue

    number = number_cell.get_text(strip=True)
    title = link.get("title") or link.get_text(" ", strip=True)
    date = date_cell.get_text(" ", strip=True)

    ids.append(number)
    titles.append(title)
    dates.append(date)

ids.extend(["5", "1"])
titles.extend(["Smallest multiple", "Multiples of 3 or 5"])
dates.extend(["Completed when dinosaurs roamed the earth.", "Completed a long, long time ago."])

def find_solution_locations(problem_id: int, root: Path = Path("..")) -> list[Path]:
    name = f"projeul_pr{problem_id}"
    locations = []

    for directory in root.iterdir():
        if not directory.is_dir() or directory.name.startswith("."):
            continue

        for path in directory.iterdir():
            if (path.is_file() and path.stem == name) or \
                (path.is_dir() and path.name == name):
                locations.append(path.relative_to(".."))

    return locations

headers = ["Problem", "Title", "Solution", "Date"]

rows = [
    [
        f"**{id}**",
        f"[{title}](https://projecteuler.net/problem={id})",
        ",".join(f"[&lt;/&gt;]({loc})" for loc in find_solution_locations(id)),
        date,
    ]
    for id, title, date in zip(ids, titles, dates)
]

widths = [
    max(len(header), max((len(row[i]) for row in rows), default=0))
    for i, header in enumerate(headers)
]

# "| Problem |  Title | Solution | Completed |"
# "|:-------:|:------:|:--------:|:---------:|"
lines = [
     "| " + " | ".join(f"{h}".ljust(w) for h,w in zip(headers, widths)) + " |",
     "|:" + ":|:".join([f"-"*w  for w in widths]) + ":|",
]

for row in rows:
    lines.append("| " + " | ".join(c.ljust(w) for c,w in zip(row, widths)) + " |")

print(f"## {solved} problems down, {remaining}+ more to go!\n")
print("\n".join(lines) + "\n")