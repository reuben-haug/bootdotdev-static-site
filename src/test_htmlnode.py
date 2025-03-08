import unittest

from src.htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a text node")
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, None, None)")
    
    def test_repr_children(self):
        node = HTMLNode("div", "This is a text node", [HTMLNode("p", "This is a paragraph")])
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, [HTMLNode(p, This is a paragraph, None, None)], None)")

    def test_repr_props(self):
        node = HTMLNode("div", "This is a text node", None, {"class": "container"})
        self.assertEqual(node.__repr__(), "HTMLNode(div, This is a text node, None, {'class': 'container'})")

if __name__ == "__main__":
    unittest.main()