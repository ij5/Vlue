from ast import *

a = parse('print(1+1)')
node = Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[BinOp(left=Num(n=1), op=Add(), right=Num(n=1))], keywords=[]))])

node.lineno = 1
node.col_offset = 1

print(dump(a))
final = compile(node, '<string>', 'exec')
exec(final)