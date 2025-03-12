# src/test_markdown_to_blocks.py

import unittest
from src.markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is a **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items

    1. Th1s 1s an ordered list
    2. with items
    3. and numb3rs
    """

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
                "1. Th1s 1s an ordered list\n2. with items\n3. and numb3rs",
            ],
    )

    def test_markdown_to_blocks_empty(self):
        md = ""

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_markdown_to_blocks_no_newline(self):
        md = "This is a **bolded** paragraph"

        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a **bolded** paragraph"])

    