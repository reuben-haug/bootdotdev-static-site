# src/test_block_to_block_type.py

import unittest

from src.block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        test_cases = [
            ("This is a paragraph", BlockType.PARAGRAPH),
            ("# Heading", BlockType.HEADING),
            ("###### Heading", BlockType.HEADING),
            ("```python\nprint('Hello, World!')\n```", BlockType.CODE),
            ("> This is a quote", BlockType.QUOTE),
            ("- This is an unordered list", BlockType.UNORDERED_LIST),
            ("1. This is an ordered list", BlockType.ORDERED_LIST),
        ]
        for block, expected_type in test_cases:
            with self.subTest(block=block):
                self.assertEqual(block_to_block_type(block), expected_type)

    def test_block_to_block_type_empty(self):
        block = ""
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_mixed(self):
        block = "This is a paragraph\n# Heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    