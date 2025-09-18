from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(markdown_block): #Takes a single block of markdown text as input and returns the BlockType representing the type of block it is.
    if is_heading(markdown_block):
        return BlockType.HEADING
    elif is_code(markdown_block):
        return BlockType.CODE
    elif is_quote(markdown_block):
        return BlockType.QUOTE
    elif is_unordered_list(markdown_block):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(markdown_block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


def is_ordered_list(markdown_block):
    lines = markdown_block.splitlines()
    for i, line in enumerate(lines):
        expected = f"{i+1}. "
        if not line.startswith(expected) or len(line) <= len(expected):
            return False
    return True
def is_heading(markdown_block):
    i = 0
    while i < len(markdown_block) and markdown_block[i] == "#":
        i += 1
        if 1 <= i and i <= 6:
            if len(markdown_block) > i:
                if markdown_block[i] == " ":
                    if len(markdown_block) > i+1:
                        return True
    return False
def is_code(block):
    return block.startswith("```") and block.endswith("```")
def is_quote(block):
    return all(line.startswith(">") for line in block.splitlines() if line != "")
def is_unordered_list(block):
    return all(line.startswith("- ") and len(line) > 2 for line in block.splitlines() if line != "")
