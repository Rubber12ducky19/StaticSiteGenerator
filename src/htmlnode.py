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

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props) #Does the parents __init__ method on the child's values.

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All Parent Nodes must have a tag")
        if not self.children:
            raise ValueError("All Parent Nodes must have a child")
        if len(self.children) == 0:
            raise ValueError("All Parent Nodes must have atleast one child")
        children_result = []
        for child in self.children:
            children_result.append(child.to_html())
        children_html = "".join(children_result)
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
        