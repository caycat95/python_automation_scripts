import os
import shutil
from pathlib import Path
from collections import defaultdict

def extension_sort(folder_path):

    # Get path to folder
    folder = Path(folder_path)
    if not folder.exists():
        print(f"Folder not found: {folder}")
        return
    
    # Categorize files by extension
    file_types = defaultdict(list)
    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix.lower().strip('.')
            file_types[ext].append(file)

    # Create subfolders and move files
    for ext, files in file_types.items():
        subfolder = folder / (ext if ext else 'others')
        subfolder.mkdir(exist_ok=True)
        for file in files:
            shutil.move(str(file), str(subfolder/file.name))

    print("Finished organizing!")
    for ext, files in file_types.items():
        print(f"Moved {len(files)} .{ext} files to /{ext}")

if __name__ == "__main__":
    path = input("Enter the path to the folder to organize: ")
    extension_sort(path)