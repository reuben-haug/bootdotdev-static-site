# tests/test_htmlnode.py

import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("span", "grandchild")
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("b", [child_node])
        self.assertEqual(parent_node.to_html(), "<b><div><span>grandchild</span></div></b>")

    def test_leaf_node_img_tag(self):
        node = LeafNode("img", None, {"src": "image.jpg", "alt": "alt text"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="alt text">')

    def test_to_html_no_value(self):
        parent_node = ParentNode("img", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_tag(self):
        parent_node = ParentNode(None, [LeafNode("span", "child")])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_props(self):
        parent_node = ParentNode("div", [LeafNode("span", "child")], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')


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