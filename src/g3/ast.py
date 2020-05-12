import re
str = """
Hello World!
\tasd
\tasdasd
\tasd"""
str = re.sub("\n", "\n\t", str)
def asd():
    print("Hello World!")
print(asd)

filename = []
filename.append(open("test.txt", 'w', encoding='UTF-8'))
filename.append(open("test2.txt", 'w', encoding='UTF-8'))
filename[0].write("Helo")
filename[1].write("Hello")
