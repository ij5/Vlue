from ast import *
import codegen

node = parse("def a():\
\tprint(1)\
")
print(dump(node))
a = [[1]]
a = a[0]
print(a)

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(codegen.to_source(tree))