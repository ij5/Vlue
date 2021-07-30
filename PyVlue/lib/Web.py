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
    def __init__(self, html=""):
        self.html = html
        self.html = self.html + "\n<style>\n"

    def apply(self):
        self.html = self.html + "\n</style>\n"
        return self.html

    def custom(self, css):
        self.html = self.html + css
        return css

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
    def __init__(self, html=""):
        self.html = html
        self.html = self.html + "\n<script>\n"

    def apply(self):
        self.html = self.html + "\n</script>\n"
        return self.html

    def custom(self, js):
        self.html = self.html + js
        return js

    def onClick(self, selector, do):
        self.html = self.html + f"""
var ___onclick = document.querySelectorAll("{selector}");
for (i=0; i < ___onclick.length; i++){{
    ___onclick[i].addEventListener('click', function(){{
        {do}
    }});
}}
"""


class Page():
    def __init__(self, body=""):
        self._head = "<head>"
        self._body = "<body>"+body

    def apply(self):
        html = self._body + "</body>"
        html = self._head + html
        html = "<html>" + html + "</html>"
        return html

    def body(self, _body):
        self._body = self._body + _body
        return _body

    def head(self, _head):
        self._head = self._head + _head
        return _head


def onexit():
    pass

atexit.register(onexit)