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

    def apply(self):
        self.html = self.html + "\n</style>\n"
        return self.html

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
        temp = f"""
{selector}{{
    height: {height};
}}
"""
        self.html = self.html + temp
        return temp

    def setMargin(self, selector, margin):
        temp = f"""
{selector}{{
    margin: {margin};
}}
"""
        self.html = self.html + temp
        return temp

    def setPadding(self, selector, padding):
        self.html = self.html + f"""
{selector}{{
    padding: {padding};
}}
"""


class Script():
    def __init__(self, html):
        self.html = html
        self.html = self.html + "\n<script>\n"

    def apply(self):
        self.html = self.html + "\n</script>\n"
        return self.html

    def onClick(self, selector, do):
        self.html = self.html + f"""
var ___onclick = document.querySelectorAll("{selector}");
for (i=0; i < ___onclick.length; i++){{
    ___onclick[i].addEventListener('click', function(){{
        {do}
    }});
}}
"""


def onexit():
    pass

atexit.register(onexit)