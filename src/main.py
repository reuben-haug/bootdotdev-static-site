# src/main.py

from .copy_static import copy_static
from .generate_page import generate_pages_recursive

def main():
    copy_static()
    # Generate a page from content/index.md using template.html to public/index.html
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()