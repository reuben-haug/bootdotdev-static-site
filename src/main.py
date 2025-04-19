# src/main.py

import sys
from .copy_static import copy_static
from .generate_page import generate_pages_recursive

default_basepath = "/"
src_dir = "./content"
template_file = "./template.html"
dest_dir = "./docs"

def main():
    basepath = default_basepath

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_static()
    # Generate a page from content/index.md using template.html to public/index.html
    generate_pages_recursive(basepath, src_dir, template_file, dest_dir)

if __name__ == "__main__":
    main()