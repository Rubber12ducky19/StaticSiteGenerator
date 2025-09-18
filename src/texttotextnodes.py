from splitnodes import split_nodes_image, split_nodes_link
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

def text_to_textnodes(text):
    new_nodes = []
    text_node = TextNode(text,TextType.TEXT)
    #print(text_node)
    new_nodes.append(text_node)
    image_text = split_nodes_image(new_nodes)
    link_text = split_nodes_link(image_text)
    bold_text = split_nodes_delimiter(link_text,"**",TextType.BOLD)
    italic_text = split_nodes_delimiter(bold_text, "_",TextType.ITALIC)
    code_text = split_nodes_delimiter(italic_text, "`", TextType.CODE)
    return code_text
