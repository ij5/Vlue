from ast import *
import codegen

node = parse("def a(a):\
\tprint(1)\
")
print(dump(node))
__ = [[1]]
__ = __[0]
print(__)

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(codegen.to_source(tree))
