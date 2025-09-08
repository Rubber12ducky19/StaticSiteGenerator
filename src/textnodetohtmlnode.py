from textnode import TextType
from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None,text_node.text,None)
        case TextType.BOLD:
            return LeafNode("b",text_node.text,None)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text,None)
        case TextType.CODE:
            return LeafNode("code", text_node.text,None)
        case TextType.LINK:
            if text_node.url:
                return LeafNode("a",text_node.text, {"href":text_node.url})
            raise Exception("Link in text_node has no url")
        case TextType.IMAGE:
            if text_node.url:
                return LeafNode("img", "",{"src":text_node.url, "alt": text_node.text})
            raise Exception("Image in text_node has no url")
        case _:
            raise Exception("text_node has no supporting TextType enum")