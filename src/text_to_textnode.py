# src/text_to_textnode.py

from src.textnode import TextNode, TextType
from src.split_delimiter import split_nodes_delimiter, split_nodes_images, split_nodes_links

def text_to_textnodes(text):
    """
    Returns a string of markdown text as a list of TextNode objects.  Empty strings are returned as a single TextNode object.
    """

    if text == "":
        return [TextNode("", TextType.TEXT)]

    # Start with a single text node containing the entire text
    nodes = [TextNode(text, TextType.TEXT)]

    # Process different markdown syntax types in sequence.  Order is important to avoid conflicts.

    # Bold text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)

    # Italic text
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    # Code blocks
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    # Images 
    nodes = split_nodes_images(nodes)

    # Links
    nodes = split_nodes_links(nodes)

    return nodes