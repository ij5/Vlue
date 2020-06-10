from ast import *

class Expr(Module):
    def __init__(self):
        pass


class BinOp(Expr):
    def __init__(self, left, op, right):
        self.left = left
        self.right = right
        self.op = op

a = BinOp(Constant(value=8), Add(), Constant(value=3))
print(dump(a))