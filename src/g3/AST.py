import ast

node = ast.FunctionDef('function', ['a'], 'print("Hello World!")')
node.lineno = 0
node.col_offset = 0
node = ast.Module([node])
code = compile(node, '<string>', 'exec')
print(ast.dump(node))

#compile(a, '<string>', 'exec')