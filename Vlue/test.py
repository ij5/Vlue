from ast import *

string = """
@route()
def Hello():
    pass
"""
a = parse(string)
print(dump(a))