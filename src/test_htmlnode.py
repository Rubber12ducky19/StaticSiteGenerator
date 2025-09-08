import unittest

from src.htmlnode import HTMLNode, LeafNode, ParentNode
class HTMLNode(unittest.TestCase):
    def test_eq(self):
        node = {
            "href": "https://www.google.com",
            "target": "_blank",
            }#Adds some test cases
        node2 = {
        "href": "https://www.google.com",
        "target": "_blank",
        }#Another test case, the same as the first.
        self.assertEqual(node, node2) #if the inputs are equal the test passes
        node3 = {
            "href": "https://www.yahoo.com",
            "target": "_blank",
            }
        node4 = {
        "href": "https://www.gooogle.com",
        "target": "_blank",
}
        node5 = {
        "href": "https://www.twitter.com",
        "target": "X is not Twitter",
}
        self.assertNotEqual(node, node5) #if the inputs are not equal the test passes
        self.assertNotEqual(node3,node4)
        self.assertNotEqual(node5,node3)
        self.assertNotEqual(node, node4)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node_p = LeafNode("p", "Hello, world!")
        self.assertEqual(node_p.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_b(self):
        node_b = LeafNode("b", "Hello, world!")
        self.assertEqual(node_b.to_html(), "<b>Hello, world!</b>")
    def test_leaf_to_html_tag(self):
        with self.assertRaises(ValueError):
            LeafNode("a", None).to_html()
    def test_leaf_to_html_value(self):
        node_value = LeafNode(None,"This is a test of Value")
        self.assertEqual(node_value.to_html(), "This is a test of Value")
    def test_leaf_to_html_a(self):
        node_HTML = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node_HTML.to_html(),  '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()