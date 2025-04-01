# src/markdown_to_blocks.py

from typing import List

def markdown_to_blocks(md: str) -> List[str]:
    """
    Takes a raw Markdown string and returns a list of block strings.  Used by the markdown_to_html_node function.

    Splits the Markdown string into blocks based on double newlines.  Each block is stripped of leading and trailing whitespace.
    Empty blocks are removed.
    This function is used to convert a Markdown document into a list of blocks for further processing.

    Args:
        md (str): The Markdown string.
    Returns:
        List[str]: A list of block strings.
    """
    
    blocks = md.split("\n\n")
    filtered_blocks = []
    # Remove empty blocks and strip whitespace
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)

    return filtered_blocks