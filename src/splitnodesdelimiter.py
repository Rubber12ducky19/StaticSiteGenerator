from textnode import TextNode, TextType
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #Takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, where any "text" type nodes in the input list are(potentially) 
    # split into multiple nodes based on the syntax.

    #Example: node = TextNode("This is a text with a  'code block' word", TextType.TEXT)
        #new nodes = split_nodes_delimiter([node], "`", TextType.Code)
        #
        #new nodes becomes: [
            #TextNode("This is a text with a ", TextType.Text),
            #TextNode("code block", TextType.Code),
            #TextNode("word", TextType.Text)
            # ]
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type is TextType.TEXT: #Checks if a node is the TextType.TEXT
            node_list = node.text.split(delimiter) #Breakes node.text into a list by the delimiter
            if len(node_list) % 2 == 0: #Checks to see if the text is closing by the delimiter(invalid code)
                raise Exception("Delimiter not closing")
            for index in range(len(node_list)):
                if node_list[index] != "":#If there is any text.
                    if index % 2 == 0:
                        new_nodes.append(TextNode(node_list[index],TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(node_list[index],text_type))
            
        else:
            new_nodes.append(node)#Adds the non-TextType.Text    
    return new_nodes
        

