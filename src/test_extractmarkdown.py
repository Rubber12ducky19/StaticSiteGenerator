
import unittest
from extractmarkdown import extract_markdown_images, extract_markdown_links
class test_extractmarkdown(unittest.TestCase):

    def test_extract_markdown_images(self):
        print("'Extract MD Images:'")
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        print("-Passed")
        print("'Extract MD Images Multi:'")
        matches = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
        print("-Passed")
    
    def test_extract_markdown_links(self):
        print("'Extract MD Links:'")
        matches = extract_markdown_links(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)
        print("-Passed")
        print("'Extract MD Links Multi:'")
        matches = extract_markdown_links("This is text with a [Yahoo](https://www.yahoo.com) and [Google](https://www.google.com)")
        self.assertListEqual([("Yahoo", "https://www.yahoo.com"), ("Google", "https://www.google.com")], matches)
        print("-Passed")