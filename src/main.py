#./main.sh
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode, ParentNode

def main():
    test = TextNode("This is a test", TextType.TEXT,)
    print (test)


print ("hello world")
main()