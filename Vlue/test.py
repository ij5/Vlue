from ast import *

string = "a.b = 3"
a = parse(string)
print(dump(a))