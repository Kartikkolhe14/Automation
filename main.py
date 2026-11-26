"""Smart File Organizer
Scans a folder, looks at each file's extension, creates category folders,
and moves files into the right folder.

Usage:
    python main.py                 # organizes ./sample_files
    python main.py path/to/folder  # organizes any folder
"""

import shutil
import sys
from pathlib import Path

# Map folder name -> list of extensions that belong in it
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".pptx"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}


# Step 4: Identify the file extension -> category
def get_category(file_path: Path) -> str:
    extension = file_path.suffix.lower()  # ".JPG" -> ".jpg"
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


# Avoid overwriting a file that already exists in the destination
def unique_destination(destination: Path) -> Path:
    if not destination.exists():
        return destination
    counter = 1
    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        candidate = destination.with_name(new_name)
        if not candidate.exists():
            return candidate
        counter += 1


def organize_folder(folder: Path) -> None:
    if not folder.is_dir():
        print(f"Error: '{folder}' is not a folder.")
        return

    moved = 0

    # Step 3: Scan files in the folder (only files, not sub-folders)
    for item in folder.iterdir():
        if not item.is_file():
            continue
        if item.name == Path(__file__).name:  # never move this script
            continue

        category = get_category(item)

        # Step 5: Create the category folder if it doesn't exist
        target_folder = folder / category
        target_folder.mkdir(exist_ok=True)

        # Step 6: Move the file
        destination = unique_destination(target_folder / item.name)
        shutil.move(str(item), str(destination))
        print(f"Moved: {item.name:<25} -> {category}/")
        moved += 1

    print(f"\nDone! {moved} file(s) organized.")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sample_files")
    organize_folder(target)