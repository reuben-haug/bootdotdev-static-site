# src/split_delimiter.py

from src.textnode import TextNode, TextType
from typing import List

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    # Returns a list of new nodes, where any 'text' type nodes in the input list are (potentially) split into multiple nodes based on the markdown syntax.  If the delimiter is not found in a text node, the node is returned as-is.
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # Split text by delimiter
        split_text = node.text.split(delimiter)
        # If no delimiter was found, keep the node as-is
        if len(split_text) == 1:
            new_nodes.append(node)
            continue
        for i, text in enumerate(split_text):
            if text == "":
                continue
            # Even indices are regular text
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            # Odd indices are formatted according to text type
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes