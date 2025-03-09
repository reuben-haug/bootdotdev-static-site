# src/split_delimiter.py

from src.textnode import TextNode, TextType
from src.markdown_parser import extract_markdown_images, extract_markdown_links
from typing import List

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType) -> List[TextNode]:
    """
    Returns a list of new nodes, where any 'text' type nodes in the input list are (potentially) split into multiple nodes based on the markdown syntax.  If the delimiter is not found in a text node, the node is returned as-is.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        split_text = node.text.split(delimiter)
        if len(split_text) == 1:
            new_nodes.append(node)
            continue
            
        for i, text in enumerate(split_text):
            if text == "":
                continue
                
            if i % 2 == 0:
                new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(TextNode(text, text_type))
    return new_nodes

def split_nodes_images(old_nodes: List[TextNode]) -> List[TextNode]:
    """
    Split text nodes containing markdown image syntax ![alt](url) into separate text and image nodes.
    Uses extract_markdown_images to process each text node.
    """
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        extracted_tuples = extract_markdown_images(old_node.text)
        
        if len(extracted_tuples) == 0:
            new_nodes.append(old_node)
        else:
            remaining_text = old_node.text
            
            for alt_text, url in extracted_tuples:
                image_markdown = f"![{alt_text}]({url})"
                parts = remaining_text.split(image_markdown, 1)
                
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                
                remaining_text = parts[1] if len(parts) > 1 else ""
            
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes

def split_nodes_links(old_nodes: List[TextNode]) -> List[TextNode]:
    """
    Split text nodes containing markdown link syntax [text](url) into separate text and link nodes.
    Uses extract_markdown_links to process each text node.
    """
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        extracted_tuples = extract_markdown_links(old_node.text)
        
        if len(extracted_tuples) == 0:
            new_nodes.append(old_node)
        else:
            remaining_text = old_node.text
            
            for link_text, url in extracted_tuples:
                link_markdown = f"[{link_text}]({url})"
                parts = remaining_text.split(link_markdown, 1)
                
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
                
                new_nodes.append(TextNode(link_text, TextType.LINK, url))
                
                remaining_text = parts[1] if len(parts) > 1 else ""
            
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    
    return new_nodes
