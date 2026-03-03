import yaml
from pathlib import Path
import os
from src.textSummarizerWebApplication.logging import logger


def read_Yaml_File(file_path: Path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        logger.info(f"{file_path} Yaml File read successfully")
    return data

def create_folder(file_path: Path ):
    try:
        os.makedirs(file_path)
        logger.info(f"Nested directories '{file_path}' created successfully.")
    except FileExistsError:
        logger.info(f"One or more directories in '{file_path}' already exist.")
    except PermissionError:
        logger.info(f"Permission denied: Unable to create '{file_path}'.")
    except Exception as e:
        logger.info(f"An error occurred: {e}")
