import ast

a = ast.FunctionDef('test', 'a,b', 'print("Hello World!")')
b = ast.Call('test')
c = ast.NodeTransformer()
print(ast.dump(a))
print(ast.dump(b))
compile(a, '<string>', 'exec')