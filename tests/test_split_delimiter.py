# src/test_split_delimiter.py

import unittest

from src.textnode import TextNode, TextType
from src.split_delimiter import split_nodes_delimiter, split_nodes_images, split_nodes_links

class TestSplitDelimiter(unittest.TestCase):
    def test_different_delimiters(self):
        test_cases = [
        # (input text, delimiter, text_type, expected_node_count, expected_types)
        ("This is **bold** text", "**", TextType.BOLD, 3, [TextType.TEXT, TextType.BOLD, TextType.TEXT]),
        ("This is _italic_ text", "_", TextType.ITALIC, 3, [TextType.TEXT, TextType.ITALIC, TextType.TEXT]),
        ("This is `code` text", "`", TextType.CODE, 3, [TextType.TEXT, TextType.CODE, TextType.TEXT]),
        ]

        for input_text, delimiter, text_type, expected_node_count, expected_types in test_cases:
            with self.subTest(input_text=input_text, delimiter=delimiter, text_type=text_type):
                nodes = [TextNode(input_text, TextType.TEXT)]
                result = split_nodes_delimiter(nodes, delimiter, text_type)
                self.assertEqual(len(result), expected_node_count)
                for i, expected_types in enumerate(expected_types):
                    self.assertEqual(result[i].text_type, expected_types)

class TestSplitNodesImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_images([node])
        self.assertListEqual([node], new_nodes)

    def test_split_start_image(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.wikipedia.org)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.wikipedia.org"),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_links([node])
        self.assertListEqual([node], new_nodes)

    def test_split_start_link(self):
        node = TextNode("[link](https://www.wikipedia.org)",
            TextType.TEXT
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.wikipedia.org")
            ],
            new_nodes,
        )
