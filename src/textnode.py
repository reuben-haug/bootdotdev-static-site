# src/textnode.py
from enum import Enum
from src.htmlnode import LeafNode

# Enum for inline text
class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(self):
    if self.text_type not in TextType:
        raise ValueError("Invalid text type")
    if self.text_type == TextType.TEXT:
        return LeafNode(None, self.text)
    if self.text_type == TextType.BOLD:
        return LeafNode("b", self.text)
    if self.text_type == TextType.ITALIC:
        return LeafNode("i", self.text)
    if self.text_type == TextType.CODE:
        return LeafNode("code", self.text)
    if self.text_type == TextType.LINK:
        return LeafNode("a", self.text, {"href": self.url})
    if self.text_type == TextType.IMAGE:
        return LeafNode("img", None, {"src": self.url, "alt": self.text})