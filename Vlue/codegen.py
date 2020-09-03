from ast import *


class Node():
    def __init__(self):
        pass

    def identifier(self, identifier):
        self.identifier = identifier

class HTML(NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        NodeVisitor.generic_visit(self, node)

    def visit_IDENTIFIER(self, node):
        print("IDENTIFIER: ", node.identifier)

if __name__=="__main__":
    node = Node()
    node.identifier("html")

    html = HTML()
    html.visit(node)

