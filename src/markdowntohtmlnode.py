from markdowntoblocks import markdown_to_blocks
from blocktype import block_to_block_type,BlockType
from texttotextnodes import text_to_textnodes
from textnodetohtmlnode import text_node_to_html_node
from textnode import TextNode,TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):#Converts a full markdown document into a single parent HTMLNode.
    #That one parent HTMLNode should contain many child HTMLNode objects representing the nested elements.
    html_children = []
    markdown_blocks = markdown_to_blocks(markdown)#Splits the markdown into blocks
    for block in markdown_blocks: #Loop over each block
        match_result = block_to_block_type(block) #Determine the type of block
        match match_result:
            case BlockType.HEADING:
               child = match_is_heading(block)
            case BlockType.CODE:
                child = match_is_code(block)
            case BlockType.QUOTE:
                child = match_is_quote(block)
            case BlockType.PARAGRAPH:
                child = match_is_paragraph(block)
            case BlockType.UNORDERED_LIST:
                child = match_is_unordered(block)
            case BlockType.ORDERED_LIST:
                child = match_is_ordered(block)
        html_children.append(child)
    return ParentNode("div",children= html_children)

def match_is_heading(block): #Since the block is a heading
    i = 0 # the index moving throug the block
    while i < len(block) and block[i] == "#": i += 1
    level = min(i, 6)
    if level == 0 or level >= len(block) or block[level] != " ": #is not a heading.
        raise Exception("block incorrectly identified as heading")
    text = block[level+1:].rstrip()
    heading_children = text_to_textnodes(text) #heading_children is a list
    html_children = []
    for child in heading_children:
        html_children.append(text_node_to_html_node(child))
    return ParentNode((f"h{level}"),children= html_children)


def match_is_code(block):

    lines = block.splitlines()
    joined_lines = "\n".join(lines[1:-1]) + "\n"
    code_leaf = LeafNode("code", joined_lines)  
    return ParentNode("pre", children= [code_leaf])

def match_is_quote(block):
    lines = block.splitlines()
    cleaned_lines = []
    for line in lines:
        if line.startswith(">"):
            cleaned_lines.append(line[1:].strip())
        else: cleaned_lines.append(line.strip())
    text="\n".join(cleaned_lines).rstrip("\n")
    quote_children = text_to_textnodes(text)
    html_quote = [text_node_to_html_node(child)for child in quote_children]
    return ParentNode("blockquote",children= html_quote)

def match_is_paragraph(block):
    trimmed = [ln.strip() for ln in block.splitlines()] #Trimmed is stripped lines for each line split from block.
    text = " ".join([ln for ln in trimmed if ln]) # Join each line back together, if they exist.
    p_children = text_to_textnodes(text)
    html_children = [text_node_to_html_node(child) for child in p_children]
    return ParentNode("p", children= html_children)

def match_is_unordered(block):
    lines = block.splitlines()
    ul_children = []
    for line in lines:
        if line.startswith("-"):
            content = line[1:].strip()
            li_child_text = text_to_textnodes(content)
            li_child_html = [text_node_to_html_node(child) for child in li_child_text]
            ul_children.append(HTMLNode("li",children = li_child_html))
    return ParentNode("ul", children= ul_children)


def match_is_ordered(block):
    lines = block.splitlines()
    ol_children = []
    i = 1
    for line in lines:
        if line != "":
            if line.startswith(f"{i}."):
                content = line[2:].strip()
                li_child = text_to_textnodes(content)
                li_child_html = [text_node_to_html_node(child) for child in li_child]
                ol_children.append(HTMLNode("li", children= li_child_html))
                i += 1
    
    return ParentNode("ol", children = ol_children)
        

