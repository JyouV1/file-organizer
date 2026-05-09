import os
import shutil
from pathlib import Path

def main():
    Documents = Path.home() / "Documents"


    extensionlist = {
        "txt" : [".txt"],
        "docx" : [".docx"],
        "ppt" : [".pptx"],
        "pdf" : [".pdf"],
        "exel" : [".xlsx"]
    }



    for folder in extensionlist :
        os.makedirs(os.path.join(Documents, folder), exist_ok=True)

    for file in os.listdir(Documents):
        file_path = os.path.join(Documents, file)
        if os.path.isfile(file_path):
            for folder, extensions in extensionlist.items():
                if any(file.endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(Documents, folder, file))
                    break

main()