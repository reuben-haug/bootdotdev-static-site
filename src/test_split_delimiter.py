# src/test_split_delimiter.py

import unittest

from src.textnode import TextNode, TextType
from src.split_delimiter import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test_different_delimiters(self):
        test_cases = [
            # (input text, delimiter, text_type, expected_node_count, expected_types)
        ("This is **bold** text", "**", TextType.BOLD, 3, [TextType.TEXT, TextType.BOLD, TextType.TEXT]),
        ("This is _italic_ text", "_", TextType.ITALIC, 3, [TextType.TEXT, TextType.ITALIC, TextType.TEXT]),
        ("This is `code` text", "`", TextType.CODE, 3, [TextType.TEXT, TextType.CODE, TextType.TEXT])
        ]

        for input_text, delimiter, text_type, expected_node_count, expected_types in test_cases:
            with self.subTest(input_text=input_text, delimiter=delimiter, text_type=text_type):
                nodes = [TextNode(input_text, TextType.TEXT)]
                result = split_nodes_delimiter(nodes, delimiter, text_type)
                self.assertEqual(len(result), expected_node_count)
                for i, expected_types in enumerate(expected_types):
                    self.assertEqual(result[i].text_type, expected_types)