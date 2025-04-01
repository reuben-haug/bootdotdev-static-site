# src/markdown_to_html_node.py

from typing import List
from src.block_to_block_type import BlockType, block_to_block_type
from src.htmlnode import HTMLNode, ParentNode, LeafNode
from src.markdown_to_blocks import markdown_to_blocks
from src.text_to_textnode import text_to_textnodes

'''
Convert a full markdown document to an HTML node.  The HTML node may contain many child HTMLNode objects representing nested HTML elements.
'''

def markdown_to_html_node(md: str) -> HTMLNode:
    """Convert markdown to an HTML node.  The HTMLNode may contain many child HTMLNode objects representing nested HTML elements.
    
    Args:
        md (str): The markdown string.
    Returns:
        HTMLNode: The HTML node representing the markdown."""
    if md == "":
        return ParentNode("div", [])
    # Split the markdown into blocks
    blocks = markdown_to_blocks(md)
    parent = ParentNode("div", [])
    
    # Process each block and add to parent
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            parent.children.append(block_to_paragraph(block))
        elif block_type == BlockType.HEADING:
            parent.children.append(block_to_heading(block))
        elif block_type == BlockType.CODE:
            parent.children.append(block_to_code(block))
        elif block_type == BlockType.QUOTE:
            parent.children.append(block_to_quote(block))
        elif block_type == BlockType.UNORDERED_LIST:
            parent.children.append(block_to_unordered_list(block))
        elif block_type == BlockType.ORDERED_LIST:
            parent.children.append(block_to_ordered_list(block))
        else:
            raise ValueError(f"Invalid block type: {block_type}")
    
    print(f"Node count: {len(parent.children)}")
    # Return the parent node with all children
    return parent

def text_to_children(text: str) -> List[HTMLNode]:
    """Input text with inline markdown syntax to return a list of HTML nodes."""
    if text == "":
        return [LeafNode(None, "")]
    
    children = []
    node_list = text_to_textnodes(text)
    for node in node_list:
        children.append(node.text_node_to_html_node())

    return children

def block_to_paragraph(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML paragraph node."""
    if not block:
        raise ValueError("Invalid paragraph")
    # Remove leading and trailing newlines
    block = block.strip().replace("\n", " ")
    parent = ParentNode("p", text_to_children(block))

    return parent

def block_to_heading(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML heading node."""
    if not block.startswith("#"):
        raise ValueError("Invalid heading block")
    # Determine heading level
    level = 0
    while block[level] == "#":
        level += 1
    if level == 0 or (level < len(block) and block[level] != " "):
        raise ValueError("Invalid heading block")
    # Create the heading node
    parent = ParentNode(f"h{level}", [])
    children = text_to_children(block[level + 1:].strip())
    parent.children = children

    return parent

def block_to_code(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML code node."""
    if not block.startswith("```") and not block.endswith("```"):
        raise ValueError("Invalid code block")
    # Remove the ``` from the beginning and end of the block
    code_content = block[3:-3].strip()
    # Ensure there is always a trailing newline and add one if not
    if not code_content.endswith("\n"):
        code_content += "\n"
    code_node = LeafNode("code", code_content)
    parent = ParentNode("pre", [code_node])
    
    return parent

def block_to_quote(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML quote node."""
    if not block:
        raise ValueError("Invalid quote")
    # Remove '> ' from the beginning of each line
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("> "):
            new_lines.append(line[2:])
        else:
            new_lines.append(line)
    
    content = "\n".join(new_lines)
    parent = ParentNode("blockquote", [])
    children = text_to_children(content)
    parent.children = children
    
    return parent

def block_to_unordered_list(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML unordered list node."""
    parent = ParentNode("ul", [])
    lines = block.split("\n")
    for line in lines:
        if line.startswith("- ") or line.startswith("* "):
            item_content = line[2:]
            item_node = ParentNode("li", text_to_children(item_content))
            parent.children.append(item_node)
    if not parent.children:
        raise ValueError("Invalid unordered list block")
    
    return parent

def block_to_ordered_list(block: str) -> HTMLNode:
    """Convert a block of markdown to an HTML ordered list node."""
    parent = ParentNode("ol", [])
    lines = block.split("\n")
    for line in lines:
        # Explicitly match lines like "1. item" or "2. item"
        if len(line) > 2 and line[0].isdigit() and line[1] == "." and line[2] == " ":
            line_content = line[3:]  # Always start after the digit, period, and space
            item_node = ParentNode("li", text_to_children(line_content))
            parent.children.append(item_node)
    if not parent.children:
        raise ValueError("Invalid ordered list block")
    
    return parent

