import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Q/A"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"/{project_name}/__init__.py",
    f"dl_approch/{project_name}/paths/path.py",
    f"dl_approch/{project_name}/text_sumrize/text.py",
    #f"dl_approch/{project_name}/path/__init__.py",
    f"dl_approch/{project_name}/compents/main.py",
    f"llm_approch/{project_name}/prompts/__init__.py",
    f"llm_approch/{project_name}/paths/path.py",
    f"llm_approch/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "templates/index.html",
    "templates/index1.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")