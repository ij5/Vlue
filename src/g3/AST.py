import ast
print(ast)

a = ast.parse("1+1")
print(ast.dump(a))

node = ast.BinOp(left=ast.Num(1), op=ast.Add(), right=ast.Num(1))
node.lineno = 1
node.col_offset = -1

node = ast.Expr(node)
node.lineno = 1
node.col_offset = -1

node = ast.Module(body=[node])
node.lineno = 1
node.col_offset = -1

node = compile(node, '<string>', 'exec')