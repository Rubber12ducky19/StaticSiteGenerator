import re

def extract_markdown_images(text):
    #example = ("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
    #result = extract_markdown_images(example)
    #print(result) = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    result = re.findall(r'!\[(.+?)\]\((.+?)\)',text)
    return result

def extract_markdown_links(text):
    result = re.findall(r'\[(.+?)\]\((.+?)\)',text)
    return result