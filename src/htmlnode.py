# src/htmlnode.py
class HTMLNode:
    def __init__(self, tag, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method must be implemented")

    def props_to_html(self):
        # Return a string of the properties in the format key="value".  The properties should be separated by a space.
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        else:
            # Recursively call to_html on each child and join the results.  Nest the children in the parent tag.
            children_html = "".join([child.to_html() for child in self.children])
            if self.props is None:
                return f"<{self.tag}>{children_html}</{self.tag}>"
            else:
                return f"<{self.tag} {self.props_to_html()}>{children_html}</{self.tag}>"


    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        # Return the HTML representation of the LeafNode.
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            # Add white space between the tag and the properties
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
            