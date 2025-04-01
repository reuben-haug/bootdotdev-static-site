# tests/test_block_html_node_helpers.py

from src.markdown_to_html_node import text_to_children

import unittest

class TestBlockHtmlNodeHelpers(unittest.TestCase):
    
    def test_text_to_children(self):
        node_list = text_to_children("This is **bold** and _italic_ text with `code`")
        html_nodes = [node.to_html() for node in node_list]
        self.assertEqual(html_nodes, [
            "This is ",
            "<b>bold</b>",
            " and ",
            "<i>italic</i>",
            " text with ",
            "<code>code</code>"
        ])

    def test_text_to_children_empty(self):
        node_list = text_to_children("")
        self.assertEqual(len(node_list), 1)

    def test_text_to_children_plain(self):
        node_list = text_to_children("Just plain text")
        html_nodes = [node.to_html() for node in node_list]
        self.assertEqual(html_nodes, ["Just plain text"])