from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    #example = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
    #result = split_nodes_link([example])
        #[TextNode("This is text with a link ", TextType.TEXT),
        #TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        #TextNode(" and ", TextType.TEXT),
        #TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text

        while True: #Starts a loop

            imgs = extract_markdown_images(remaining)#Extract the alt & url from the next
            if not imgs: #if the function comes up empty
                break #break the loop
            alt, url = imgs[0]#gets the first alt-text, url pair from the list.
            needle = f"![{alt}]({url})" #recreates the alt-text, url pair to remove from the text
            if needle not in remaining: #if the needle is not in the text
                new_nodes.append(TextNode(remaining,TextType.TEXT)) #adds the text to result
                remaining = ""
                break
            parts = remaining.split(needle,1)
            before = parts[0]
            after = parts[1] if len(parts) == 2 else ""
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.IMAGE,url))
                remaining = after
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        remaining = node.text
        while True:
            links = extract_markdown_links(remaining)
            if not links:
                break
            alt, src = links[0]
            needle = f"[{alt}]({src})"
            if needle not in remaining:
                new_nodes.append(TextNode(remaining, TextType.TEXT))
                remaining = ""
                break
            parts = remaining.split(needle,1)
            before = parts[0]
            after = parts[1] if len(parts) == 2 else ""
            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(alt, TextType.LINK,src))
                remaining = after
        if remaining:
            new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes
