from ast import *

a = parse('print(1)')
node = Module(lineno=1, col_offset=-1, body=[Expr(lineno=1, col_offset=-1, value=Call(lineno=1, col_offset=-1, func=Name(lineno=1, col_offset=-1, id='print', ctx=Load()), args=[Num(lineno=1, col_offset=-1, n=1)], keywords=[]))])

print(dump(a))
final = compile(node, '<string>', 'exec')
exec(final)