import re
str = """
Hello World!
\tasd
\tasdasd
\tasd"""
str = re.sub("\n", "\n\t", str)
print(str)