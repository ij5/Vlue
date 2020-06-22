from ast import *
import codegen
class BaseNode():
    def __init__(self, RETURN=0):
        self.RETURN = RETURN

n = BaseNode()
n.asd = "a"
print(n.asd)

node = parse("print('Hello World!'+'aa')\
")
print(dump(node))
__ = [[1]]
__ = __[0]
print(__)

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(codegen.to_source(tree))
