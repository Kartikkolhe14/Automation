"""Step 7: Creates a messy 'sample_files' folder to test main.py on."""

from pathlib import Path

SAMPLE_NAMES = [
    "holiday.jpg", "logo.PNG", "resume.pdf", "notes.txt", "report.docx",
    "budget.xlsx", "data.csv", "movie.mp4", "song.mp3", "backup.zip",
    "script.py", "index.html", "mystery.xyz", "README",
]

folder = Path("sample_files")
folder.mkdir(exist_ok=True)

for name in SAMPLE_NAMES:
    (folder / name).write_text("sample content")

print(f"Created {len(SAMPLE_NAMES)} sample files in '{folder}/'")