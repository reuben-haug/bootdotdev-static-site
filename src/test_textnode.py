import unittest

from src.textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, text, None)")

    def test_repr_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.wikipedia.org")
        self.assertEqual(node.__repr__(), "TextNode(This is a link, link, https://www.wikipedia.org)")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node 2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def check_url_none(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node.url, None)

if __name__ == "__main__":
    unittest.main()