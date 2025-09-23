#./main.sh
from textnode import TextNode, TextType
from htmlnode import LeafNode, HTMLNode, ParentNode
from file_copy import file_copy

def main():
    test = TextNode("This is a test", TextType.TEXT,)
    print (test)
    

print ("hello world")
main()
file_copy("static", "public/")