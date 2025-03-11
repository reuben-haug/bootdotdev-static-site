# src/test_block_to_block_type.py

import unittest

from src.block_type import BlockType, block_to_block_type

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