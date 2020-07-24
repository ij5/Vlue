from ast import *
from astor import code_gen
class BaseNode():
    def __init__(self, RETURN=0):
        self.RETURN = RETURN

n = BaseNode()
n.asd = "a"
print(n.asd)

node = parse('''

b.a
''')
a = compile(node, '<string>', 'exec')
print(a)
print(dump(node))
__ = [[1]]
__ = __[0]
print(__)

print("  \thello\t".strip())

tree = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])
print(code_gen.to_source(tree))

a = 2<3
print(a)
