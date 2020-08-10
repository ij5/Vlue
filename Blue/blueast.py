from ast import *
from astor import code_gen
class BaseNode():
    def __init__(self, RETURN=0):
        self.RETURN = RETURN

    def print(self, data):
        print(data)

    class test:
        def __init__(self):
            self.text = "test success"

tst = BaseNode().test()

print(tst.text)


n = BaseNode()
n.asd = "a"
print(n.asd)
n.print("Hello World!")

node = parse('''
for i in range():
    a = 0
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

from ctypes import cdll
p = cdll.LoadLibrary("p.dll")

print(p.isprime(100))