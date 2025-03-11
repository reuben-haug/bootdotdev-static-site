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
    """
    # Headings start with 1-6 '#' characters, followed by a space and then the text
    if re.match(r"^#{1,6}\s"):
        return BlockType.HEADING
        
    # Code blocks start and end with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Every line in a quote block must start with '>'
    if all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    
    # Unordered lists start with '- ' or '* '
    for line in block:
        if line.startswith("- ") or line.startswith("* "):
            return BlockType.UNORDERED_LIST
    
    '''
    Ordered line in an ordered list must start with a number, followed by a . character and space.
    '''
    pass
    # If none of the above conditions are met, the block is a normal paragraph
    else:
        pass

    