# tests/test_text_to_textnode.py

import unittest
from src.textnode import TextNode, TextType

from src.text_to_textnode import text_to_textnodes

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
    
    def test_text_to_textnodes_no_markdown(self):
        text = "This is text with no markdown"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("This is text with no markdown", TextType.TEXT)
            ],
            nodes
        )

    def test_text_to_textnodes_empty(self):
        text = ""

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("", TextType.TEXT)
            ],
            nodes
        )

    def test_text_to_textnodes_only_bold(self):
        text = "**bold**"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD)
            ],
            nodes
        )

    def test_text_to_textnodes_only_image(self):
        text = "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            nodes
        )

    def test_text_to_textnode_only_link(self):
        text = "[link](https://boot.dev)"

        nodes = text_to_textnodes(text)

        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
            ],
            nodes
        )