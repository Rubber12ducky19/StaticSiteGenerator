import unittest
from splitnodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class test_split_nodes_image(unittest.TestCase):
    def test_image(self):
        print("Split Node Image:")
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),],new_nodes,)
        print("-Passed")
    
    def test_link(self):
        print("\nSplit Node Link:")
        node2 = TextNode("This is text with a [link to google](https://www.google.com) and another [link to yahoo](https://www.yahoo.com)",TextType.TEXT,)
        new_nodes = split_nodes_link([node2])
        print(f"--Results of Function:\n{new_nodes}")
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("link to google", TextType.LINK, "https://www.google.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("link to yahoo", TextType.LINK, "https://www.yahoo.com"),]
        print(f"--Expected Results:\n{expected_result}")
        self.assertListEqual(expected_result,new_nodes,)
        print("\n-Passed")


