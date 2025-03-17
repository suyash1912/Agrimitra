import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

files = [
    "data/raw/",
    "data/external/",
    "data/processed/",
    "experiments/trials.ipynb",
    "src/__init__.py",
    "src/components/",
    "src/pipeline/",
    "src/utils/helpers.py",
    "requirements.txt",
    "Dockerfile",
    "params.yaml",
    "configs.yaml",
    ".github/workflows/cicd.yaml",
    "kubernetes/deployment.yaml",
    "mlflow/mlflow.yaml"
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
