def markdown_to_blocks(markdown):  #Takes a raw Markdown string, (represen ting a full document) as input and returns a list of block strings.
    markdown_blocks = markdown.split("\n\n")
    
    markdown_list = []
    for sentence in markdown_blocks:
        if sentence != "":
            markdown_list.append(sentence.strip())
    return markdown_list
    