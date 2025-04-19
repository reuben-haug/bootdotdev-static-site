# src/copy_static.py

import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def copy_directory(src_path: str, dest_path: str) -> None:
    '''
    Recursively copies the contents of the source directory to the destination directory.

    This function ensures that the destination directory exists, then iterates through the contents of the source directory. Files are copied directly, while subdirectories are processed recursively.

    Args:
        src_path (str): The path to the source directory.
        dest_path (str): The path to the destination directory.
    '''
    logging.info(f"Scanning and copying from: '{src_path}' to '{dest_path}'")

    # Ensure the destination directory exists
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    for item in os.scandir(src_path):
        src_item_path = os.path.join(src_path, item.name)
        dest_item_path = os.path.join(dest_path, item.name)

        if item.is_file():
            logging.info(f"Copying file: '{src_item_path}' to '{dest_item_path}'")
            shutil.copy(src_item_path, dest_item_path)
        elif item.is_dir():
            # Recursively scan the subdirectory
            copy_directory(src_item_path, dest_item_path)

def copy_static() -> None:
    '''
    Copies all the contents from the source directory ("static") to the destination directory ("public").

    This function first checks if the source directory ("static") exists. If it does not, a warning is logged, and the function exits. If the destination directory ("public") exists, it is deleted along with all its contents.  The function then recursively copies the contents of the source directory to the destination directory, preserving the directory structure.

    Args:
        None
    '''
    logging.info("Checking if the source directory exists...")
    if not os.path.exists("static"):
        logging.warning("Source directory 'static' does not exist.")
        return

    # Create destination directory if it doesn't exist
    if os.path.exists("docs"):
        logging.info("Destination directory 'docs' exists. Deleting...")
        shutil.rmtree("docs")

    # Start recursive copy
    logging.info("Starting copy from 'static' to 'docs'...")
    copy_directory("static", "docs")

    logging.info("Finished copying contents from 'static' to 'docs'.")