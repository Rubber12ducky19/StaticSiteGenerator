import unittest
from markdowntoblocks import markdown_to_blocks
#from textnode import TextNode, TextType
class test_markdown_to_blocks(unittest.TestCase):
    def test_md_to_blocks(self):
        print("\nMarkdown to Block :")
        test_node = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        expected_result = ["This is **bolded** paragraph",
                           "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                           "- This is a list\n- with items",]
        result_node = markdown_to_blocks(test_node)
        #print(f"--Results of Function:\n{result_node}")
        #print(f"--Expected Results:\n{expected_result}")
        self.assertListEqual(expected_result,result_node,)
        print("\n-Passed")