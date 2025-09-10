import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class test_split_nodes_delimiter(unittest.TestCase):
    def test_split(self):
        bold_node = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        node_test = split_nodes_delimiter(bold_node,"**",TextType.BOLD)
        self.assertEqual(node_test, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)])
        print("Split Nodes Delimiter:")
        print(" - Bold Text Test: Passed")

        italic_node = [TextNode("This is the first node with _italic words_ in it", TextType.TEXT),
                       TextNode("This is the second node with _italic text_", TextType.TEXT)]
        node_test = split_nodes_delimiter(italic_node,"_",TextType.ITALIC)
        self.assertEqual(node_test, [
            TextNode("This is the first node with ", TextType.TEXT),
            TextNode("italic words", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT),
            TextNode("This is the second node with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC)])
        print(" - Italic Mult-node Test: Passed")

        #broken_bold_node = [TextNode("This is suppose to be **broken", TextType.TEXT)]
        #node_test = split_nodes_delimiter(broken_bold_node, "**", TextType.BOLD)
        #self.assertEqual("Exception: Delimiter not closing")
        #print("- Delimiter closing Test: Passed")