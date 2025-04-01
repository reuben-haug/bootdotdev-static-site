# src/block_to_block_type.py

from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    """
    Returns the BlockType of the input block.
    

    Args:
        block (str): The input block of text.
    Returns:
        BlockType: The type of the block.
    """
    # Headings start with 1-6 '#' characters, followed by a space and then the text
    if re.match(r"^#{1,6}\s", block):
        return BlockType.HEADING
        
    # Code blocks start and end with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Every line in a quote block must start with '>'
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    
    """A block is considered to be a list if *all* lines in the block start with the corresponding character for the list type."""

    # Unordered lists start with '- ' or '* '
    if all(re.match(r"^(-|\*)\s", line) for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    
    # Ordered lists must start with a number, followed by a . character and space.
    if all(re.match(r"^\d+\.\s", line) for line in block.split("\n")):
            return BlockType.ORDERED_LIST
    
    # If none of the above conditions are met, the block is a normal paragraph
    
    return BlockType.PARAGRAPH

    