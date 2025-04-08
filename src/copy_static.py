# src/copy_static.py

import os
import shutil
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

'''
Copies all the contents from the source directory (static) to the destination directory (public).
The contents are copied recursively, and the directory structure is preserved.
'''

# Check if the source directory exists
logging.debug("Checking if the source directory exists...")

# Check if the destination directory exists
logging.debug("Checking if the destination directory exists...")

# Scan the source directory for files and directories
logging.debug("Scanning the source directory for files and directories...")

# Join path segments for source and destination
logging.debug("Joining path segments for source and destination...")

# Check if the current path is a file
logging.debug("Checking if the current path is a file...")

# Create the destination directory if it doesn't exist
logging.debug("Creating the destination directory...")

# Copy files from source to destination
logging.debug("Copying files from source to destination...")

# Remove the destination directory if needed
logging.debug("Removing the destination directory if needed...")

# os.path.exists to check for presence of source and destination directories

# try scandir() to return the list of directories
# os.path.join() to join the path segments

# os.path.isfile(path) returns True if path is an existing file 

# os.mkdir(path, mode=0o777, *, dir_fd)

# shutil.copy(src, dst)

# shutil.rmtree(path)