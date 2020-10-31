import atexit
from bottle import run, template, route

class Web():
    def __init__(self):
        self.port = 8000
        self.host = 'localhost'

    def start(self):
        run(host=self.host, port=self.port)



def onexit():
    pass

atexit.register(onexit)