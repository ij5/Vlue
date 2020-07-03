from ast import *
from astor import code_gen
class BaseNode():
    def __init__(self, RETURN=0):
        self.RETURN = RETURN

n = BaseNode()
n.asd = "a"
print(n.asd)

node = parse("a[1]\
")
print(dump(node))
__ = [[1]]
__ = __[0]
print(__)

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(code_gen.to_source(tree))
