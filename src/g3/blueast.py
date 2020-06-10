from ast import *

a = parse('def fn(a,b):\n\t1+1')


print(dump(a))
final = compile(node, '<string>', 'exec')
exec(final)