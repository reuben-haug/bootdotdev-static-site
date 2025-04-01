# tests/test_markdown_to_html_node.py

import unittest

from src.markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )

    def test_different_headings(self):
        test_cases = [
            # (input markdown, expected HTML)
            ("# Heading 1", "<h1>Heading 1</h1>"),
            ("## Heading 2", "<h2>Heading 2</h2>"),
            ("### Heading 3", "<h3>Heading 3</h3>"),
            ("#### Heading 4", "<h4>Heading 4</h4>"),
            ("##### Heading 5", "<h5>Heading 5</h5>"),
            ("###### Heading 6", "<h6>Heading 6</h6>")
        ]
        for input_markdown, expected_html in test_cases:
            with self.subTest(input_markdown=input_markdown):
                node = markdown_to_html_node(input_markdown)
                html = node.to_html()
                self.assertEqual(html, f"<div>{expected_html}</div>")
                
    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        )

    def test_quote(self):
        md = """
> This is a quote
> with multiple lines

> This is another quote
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><blockquote>This is a quote\nwith multiple lines</blockquote><blockquote>This is another quote</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. Item 1
2. Item 2
3. Item 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><ol><li>Item 1</li><li>Item 2</li><li>Item 3</li></ol></div>"
        )
    def test_mixed(self):
        md = """
# This is a heading

## This is a subheading

This is a paragraph with **bold** and _italic_ text.

```
This is a code block
```

> This is a quote

- Item 1
- Item 2

1. Item 1
2. Item 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()

        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1><h2>This is a subheading</h2><p>This is a paragraph with <b>bold</b> and <i>italic</i> text.</p><pre><code>This is a code block\n</code></pre><blockquote>This is a quote</blockquote><ul><li>Item 1</li><li>Item 2</li></ul><ol><li>Item 1</li><li>Item 2</li></ol></div>"
        )
    def test_empty(self):   
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div></div>")
