import atexit
from bottle import run, template, route

class Web():
    def __init__(self):
        self.port = 8000
        self.host = 'localhost'

    def start(self):
        try:
            run(host=self.host, port=self.port)
        except KeyboardInterrupt:
            print("Program ended.")

class Style():
    def __init__(self, html):
        self.html = html
        self.html = self.html + "\n<style>\n"

    def setColor(self, selector, color):
        self.html = self.html + f"""
{selector}{{
    color: {color};
}}
"""

    def setWidth(self, selector, width):
        self.html = self.html + f"""
{selector}{{
    width: {width};
}}
"""

    def setHeight(self, selector, height):
        self.html = self.html + f"""
{selector}{{
    height: {height};
}}
"""

    def setMargin(self, selector, margin):
        self.html = self.html + f"""
{selector}{{
    margin: {margin};
}}
"""



    def apply(self):
        self.html = self.html + "\n</style>"
        return self.html



class Script():
    pass


def onexit():
    pass

atexit.register(onexit)