from ast import *
import codegen

node = parse("if(a):\n\tprint(1)\nelse:\n\tprint(1)\n")
print(dump(node))

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(codegen.to_source(tree))