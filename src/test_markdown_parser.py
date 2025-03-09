# src/test_markdown_parser.py

import unittest

from src.markdown_parser import extract_markdown_images, extract_markdown_links

class TestMarkdownParser(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.wikipedia.org)"
        )
        self.assertListEqual([("link", "https://www.wikipedia.org")], matches)

    def test_extract_multiple_markdown_image(self):
        matches = extract_markdown_images(
            "This is text with two images, ![image1](https://i.imgur.com/zjjcJKZ.png) and ![image2](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [
                ("image1", "https://i.imgur.com/zjjcJKZ.png"),
                ("image2", "https://i.imgur.com/zjjcJKZ.png")
            ],
            matches
        )

    def test_extract_multiple_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with two links, [link1](https://www.wikipedia.org) and [link2](https://www.wikipedia.org)"
        )
        self.assertListEqual(
            [
                ("link1", "https://www.wikipedia.org"),
                ("link2", "https://www.wikipedia.org")
            ],
            matches
        )