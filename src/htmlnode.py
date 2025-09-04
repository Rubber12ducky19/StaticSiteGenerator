class HTMLNode:
    def __init__(self, tag= None, value= None, children= None, props= None ):
        self.tag = tag #A string representing the HTML tag name(e.g. "p", "a", "h1", etc)
        self.value = value #A string representing the value of the HTML tag (the text inside a paragraph)
        self.children = children #A list of HTMLNode objects representing the children of this node
        self.props = props #A dictionary of key-value pairs representing the attributes of the HTML tag.
        #For example, a link <a> tag might have {"href": "https://www.google.com"}
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        if not self.props:
            return ""
        if isinstance(self.props, dict):
            parts = [f'{key}="{value}"' for key, value in self.props.items()]
            #for key, value in self.props.items():
                #parts = f'{key}="{value}"'
            return " " + " ".join(parts) #turns the list into a string with a space between each part.
        raise Exception ("This is not a dictionary")
        
    def __repr__(self):
        print(f"Tag= {self.tag}")
        print(f"Value= {self.value}")
        print(f"Children= {self.children}")
        print(f"Props+ {self.props}")

    