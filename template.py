import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, 
                    format ='[%(asctime)s: %(levelname)s: %(filename)s: %(funcname)s: %(lineno)d %(message)s:]')

project_name = "text_summarizer"
list_of_files = [
                    ".github.com/workflows/.gitkeep",
                    f"src/{project_name}/__init__.py", #constructor file to consider as local package
                    f"src/{project_name}/components/__init__.py",
                    f"src/{project_name}/utils/__init__.py",
                    f"src/{project_name}/utils/common.py",
                    f"src/{project_name}/logging/__init__.py",
                    f"src/{project_name}/config/configuration.py",
                    f"src/{project_name}/pipeline/__init__.py",
                    f"src/{project_name}/entity/__init__.py",
                    f"src/{project_name}/constants/__init__.py",
                    "config/config.yaml",
                    "params.yaml",
                    "app.py",
                    "main.py",
                    "Dockerfile",
                    "requirements.txt",
                    "setup.py",
                    "expirement/notebook.ipynb"

                ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    #Check if the directory already exists
    if filedir is not None and filedir != "":
        os.makedirs(filedir, exist_ok= True)  # create a directory if it doesn't exist
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    #check if the file already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logiing.info(f"{filename} already exists in {filedir}")