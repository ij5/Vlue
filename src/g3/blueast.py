from ast import *

class Transformer(NodeTransformer):
    pass
a = "hello"

node = parse('1.2+3.4')
Transformer.visit(node)
dump(node)

