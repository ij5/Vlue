from ast import *

a = parse('a = 1+1')
node = Module(body=[Expr(value=BinOp(left=Num(n=1), op=Add(), right=Num(n=1)))])

print(dump(a))
final = compile(node, '<string>', 'exec')
exec(final)