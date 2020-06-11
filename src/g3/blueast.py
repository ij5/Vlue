from ast import *
import codegen

node = parse("1+2")
print(dump(node))

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(codegen.to_source(tree))