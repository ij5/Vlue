from ast import *

a = parse('def fn(a,b):\n\t1+1\n\treturn 2')
node = Module(lineno=1, col_offset=1, body=[
    Expr(
        lineno=1, col_offset=1, value=Call(
            lineno=1, col_offset=1, func=Name(
                lineno=1, col_offset=1, id='print', ctx=Load()
            ), args=[
                BinOp(lineno=1, col_offset=1, left=Num(
                    lineno=1, col_offset=1, n=1
                ), op=Add(lineno=1, col_offset=1), right=Num(
                    lineno=1, col_offset=1, n=1
                ))
            ], keywords=[]
        )
    )
])

print(dump(a))
final = compile(node, '<string>', 'exec')
exec(final)