# tests/test_textnode.py
import unittest

from src.textnode import TextNode, TextType, text_node_to_html_node

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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_image(self):
        # Test image with alt text
        node = TextNode("This is an image", TextType.IMAGE, "https://www.wikipedia.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.wikipedia.org", "alt": "This is an image"})
        self.assertEqual(html_node.value, None)

    def test_text_image_no_alt(self):
        # Test image without alt text
        node = TextNode("https://www.wikipedia.org", TextType.IMAGE, "https://www.wikipedia.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.wikipedia.org", "alt": "https://www.wikipedia.org"})
        self.assertEqual(html_node.value, None)

    def test_text_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://www.wikipedia.org")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://www.wikipedia.org"})
        self.assertEqual(html_node.value, "This is a link")


if __name__ == "__main__":
    unittest.main()