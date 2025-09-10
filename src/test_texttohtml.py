import unittest
from textnodetohtmlnode import text_node_to_html_node
from textnode import TextNode, TextType


class TestTexttoHtml(unittest.TestCase):
    def test_text(self):
        node_text = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node_text)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        print("Plain Text to HTML: Passed")
        
        
        node_bold = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node_bold)
        self.assertEqual(html_node.tag,"b")
        self.assertEqual(html_node.value, "This is a bold node")
        print("Bold Text to HTML: Passed")
        
        node_italic = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node_italic)
        self.assertEqual(html_node.tag,"i")
        self.assertEqual(html_node.value, "This is a italic node")
        print("Italic Text to HTML: Passed")
        
        node_code = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node_code)
        self.assertEqual(html_node.tag,"code")
        self.assertEqual(html_node.value, "This is a code node")
        print("Code Text to HTML: Passed")

        node_link = TextNode("This is a link node", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node_link)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "www.google.com"})
        print("Link Text to HTML: Passed")

        node_image = TextNode("This is a image node", TextType.IMAGE, "www.google.com")
        html_node = text_node_to_html_node(node_image)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "www.google.com", "alt": "This is a image node"})
        print("Image Text to HTML: Passed")
