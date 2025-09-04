import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD) #Adds some test cases
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2) #if the inputs are equal the test passes
        node3 = TextNode("This is a text node", TextType.ITALIC, "www.google.com")
        node4 = TextNode("This is a bad text node",TextType.IMAGE, "www.google.com")
        node5 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node5) #if the inputs are not equal the test passes
        self.assertNotEqual(node3,node4)
        self.assertNotEqual(node5,node3)
        self.assertNotEqual(node, node4)

if __name__ == "__main__":
    unittest.main()