import re
import numpy as np

s = open("main.ion", 'r').read()
o = open("index.html", 'a')

arr = []
tokens = []

s = re.split("[\t]*", s)
print(s)