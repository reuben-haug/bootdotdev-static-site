# src/markdown_parser.py

import re
from typing import List, Tuple

def extract_title(markdown: str) -> str:
    """
    Extracts the title from the Markdown content. The title is assumed to be the first top-level heading (# Heading).

    Args:
        markdown (str): The Markdown content.
    Returns:
        str: The extracted title.
    Raises:
        Exception("No h1 header found.")
    """
    match = re.match(r"^#\s+(.+)", markdown)
    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header found.")

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    """
    Extract markdown images from the text.

    Args:
        text (str): The input text containing markdown images.
    Returns:
        List[Tuple[str, str]]: A list of tuples containing the alt text and the URL of any markdown images.
    """
    # Return a list of tuples containing the alt text and the URL of any markdown images
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(image_regex, text)

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    """
    Extract markdown links from the text.

    Args:
        text (str): The input text containing markdown links.
    Returns:
        List[Tuple[str, str]]: A list of tuples containing the anchor text and the URL of any markdown links.
        The anchor text is the text between the square brackets [] and the URL is the text between the parentheses ().
    """
    # Return a list of tuples containing the anchor text and the URL of any markdown links
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(link_regex, text)