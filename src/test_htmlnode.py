import unittest

from htmlnode import HTMLNode
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

if __name__ == "__main__":
    unittest.main()