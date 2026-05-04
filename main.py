import os
import shutil
from pathlib import Path

home = Path.home()
Documents = home / "Documents"


folders = ["txt", "docx", "ppt", "pdf", "exel"]


try:
    Documents.mkdir(parents=True, exist_ok=False)
    print("create extension folder")
except FileExistsError:
    print("extension folder already created")

for extension in folders :
    ext = Documents / extension
    ext.mkdir(parents=True, exist_ok=True)
