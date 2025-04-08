# src/copy_static.py

import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def copy_directory(src_path: str, dest_path: str) -> None:
    '''
    Recursively copies the contents of the source directory to the destination directory.
    '''
    logging.info(f"Scanning and copying from: '{src_path}' to '{dest_path}'")

    # Ensure the destination directory exists
    if not os.path.exists(dest_path):
        # logging.info(f"Creating directory: {dest_path}")
        os.makedirs(dest_path)

    for item in os.scandir(src_path):
        src_item_path = os.path.join(src_path, item.name)
        dest_item_path = os.path.join(dest_path, item.name)

        if item.is_file():
            logging.info(f"Copying file: '{src_item_path}' to '{dest_item_path}'")
            shutil.copy(src_item_path, dest_item_path)
        elif item.is_dir():
            # logging.info(f"Found directory: {src_item_path}/")
            # Recursively scan the subdirectory
            copy_directory(src_item_path, dest_item_path)

def copy_static() -> None:
    '''
    Copies all the contents from the source directory (static) to the destination directory (public).
    The contents are copied recursively, and the directory structure is preserved.  Before copying, the destination directory and its contents are deleted.
    '''

    logging.info("Checking if the source directory exists...")
    if not os.path.exists("static"):
        logging.warning("Source directory 'static' does not exist.")
        return

    # Create destination directory if it doesn't exist
    if os.path.exists("public"):
        logging.info("Destination directory 'public' exists.  Deleting...")
        shutil.rmtree("public")

    # Start recursive copy
    logging.info("Starting copy from 'static' to 'public'...")
    copy_directory("static", "public")

    logging.info("Finished copying contents from 'static' to 'public'.")