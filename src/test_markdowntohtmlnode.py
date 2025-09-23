import unittest
from markdowntohtmlnode import markdown_to_html_node


class test_markdown_to_htmlnode(unittest.TestCase):
    def test_paragraphs(self):
        print(f"Markdown to HTMLNodes: \n-*Paragraphs*-")
        test_string = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        function_result = markdown_to_html_node(test_string)
        test_result = function_result.to_html()

        compare_result = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"        
        print(f"Results:\n:{test_result}")
        print(f"Solution:\n:{compare_result}")
        self.assertEqual(test_result, compare_result)
        

    def test_codeblock(self):
        print("\n-*Code*-")
        test_string = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        function_result = markdown_to_html_node(test_string)
        test_result = function_result.to_html()
        compare_result = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
       
        print(f"Results:\n:{test_result}")
        print(f"Solution:\n:{compare_result}")
        self.assertEqual(test_result,compare_result)
