from ast import *

string = """
f"{a}"
"""
a = parse(string)
print(dump(a))