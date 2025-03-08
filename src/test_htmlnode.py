# src/test_htmlnode.py
import unittest

from src.htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a text node")
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, None, None)")
    
    def test_repr_children(self):
        node = HTMLNode("div", "This is a text node", [HTMLNode("p", "This is a paragraph")])
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, [HTMLNode(p, This is a paragraph, None, None)], None)")

    def test_repr_props(self):
        node = HTMLNode("div", "This is a text node", None, {"class": "container"})
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, None, {'class': 'container'})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_leaf_to_html_none(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

    def test_leaf_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("p", "This is a paragraph", {"class": "container"})
        self.assertEqual(node.to_html(), '<p class="container">This is a paragraph</p>')

    def test_leaf_to_html_no_tags(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), "This is a paragraph")

if __name__ == "__main__":
    unittest.main()