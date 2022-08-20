"""Remove not used files."""
import logging
import os
import shutil
from pathlib import Path

logger = logging.getLogger(__name__)

manifest = {
    "owner": ".github/CODEOWNERS",
    "license": "./LICENSE"
}

squad_choice = "{{ cookiecutter.project_squad }}"
license_choice = "{{ cookiecutter.bsd3_license.lower() }}"

# Show Values
print("\nProject Name: {{ cookiecutter.project_name }}")
print("Code Owner: {}".format(squad_choice))


exclude_files = []

if squad_choice == "No Owner":
    exclude_files.append(manifest["owner"])

if license_choice != "y":
    exclude_files.append(manifest["license"])
else:
    print("License: BDS 3")

for string_path in exclude_files:
    path = Path().cwd().joinpath(string_path)
    if path.is_dir():
        shutil.rmtree(path)
    else:
        os.remove(str(path))
