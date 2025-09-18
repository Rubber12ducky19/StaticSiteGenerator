import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class test_split_nodes_delimiter(unittest.TestCase):
    def test_split(self):
        bold_node = [TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)]
        bold_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.TEXT)]
        bold_test = split_nodes_delimiter(bold_node,"**",TextType.BOLD)
        self.assertEqual(bold_test,bold_result )
        print("Split Nodes Delimiter:\n")
        print(" - Bold Text Test: Passed\n")

        italic_node = [TextNode("This is the first node with _italic words_ in it", TextType.TEXT),
                       TextNode("This is the second node with _italic text_", TextType.TEXT)]
        italic_result = [
            TextNode("This is the first node with ", TextType.TEXT),
            TextNode("italic words", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT),
            TextNode("This is the second node with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC)]
        italic_test = split_nodes_delimiter(italic_node,"_",TextType.ITALIC)
        self.assertEqual(italic_test, italic_result )
        print(" - Italic Mult-node Test: Passed\n")

        code_node = [TextNode("This is a node with 'coding' in it", TextType.TEXT)]
        code_result = [TextNode("This is a node with ", TextType.TEXT),
                       TextNode("coding",TextType.CODE),
                       TextNode(" in it", TextType.TEXT)]
        code_test = split_nodes_delimiter(code_node,"'",TextType.CODE)
        self.assertEqual(code_test,code_result)
        print( " - Code Text Test: Passed\n")

        #broken_bold_node = [TextNode("This is suppose to be **broken", TextType.TEXT)]
        #node_test = split_nodes_delimiter(broken_bold_node, "**", TextType.BOLD)
        #self.assertEqual("Exception: Delimiter not closing")
        #print("- Delimiter closing Test: Passed")