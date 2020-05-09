import re
str = """
Hello World!
\tasd
\tasdasd
\tasd"""
str = re.sub("\n", "\n\t", str)
def asd():
    print("Hello World!")
asd()