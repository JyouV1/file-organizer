import os
import shutil
from pathlib import Path

home = Path.home()
Documents = home / "Documents"

target = Documents / "Tugas Sekolah"

folders = ["b_ind", "b_ing", "b_man", "dtjkt", "informatika", "mtk", "agama", "ppkn", "ipas", "sejarah", "seni_budaya", "literasi"]

try:
    target.mkdir(parents=True, exist_ok=False)
    print("create Tugas Sekolah directory")
except FileExistsError:
    print("directory Tugas Sekolah already created")

for mapel in folders:
    (target / mapel).mkdir(exist_ok=True)

