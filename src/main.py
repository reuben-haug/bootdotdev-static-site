# src/main.py

from .copy_static import copy_static
from .generate_page import generate_page

def main():
    copy_static()
    # Generate a page from content/index.md using template.html to public/index.html
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()