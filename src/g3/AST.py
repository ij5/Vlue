import ast
ast.Num()
node = ast.UnaryOp(ast.Constant(1), ast.Constant(2))

print(ast.dump(node))

#compile(a, '<string>', 'exec')