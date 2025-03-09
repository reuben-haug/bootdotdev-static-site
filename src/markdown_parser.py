# src/markdown_parser.py

import re

def extract_markdown_images(text):
    # Return a list of tuples containing the alt text and the URL of any markdown images
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(image_regex, text)

def extract_markdown_links(text):
    # Return a list of tuples containing the anchor text and the URL of any markdown links
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_regex, text)