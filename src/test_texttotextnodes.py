import unittest
from texttotextnodes import text_to_textnodes
from textnode import TextNode, TextType
class test_text_to_text_nodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        print("\nText to Text Node :")
        test_node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
        result_node = text_to_textnodes(test_node)
        #print(f"--Results of Function:\n{result_node}")
        #print(f"--Expected Results:\n{expected_result}")
        self.assertListEqual(expected_result,result_node,)
        print("\n-Passed")