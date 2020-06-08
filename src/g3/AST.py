import ast

node = ast.Add()
node.lineno = 0
node.col_offset = 0

node = ast.BinOp(1, node, 2)
node.lineno = 0
node.col_offset = 0

node = ast.Expr(node)
node.lineno = 0
node.col_offset = 0

node = ast.Module([node])
code = compile(node, '<string>', 'exec')
print(ast.dump(node))

#compile(a, '<string>', 'exec')