import subprocess
import atexit
import platform
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Web(BaseHTTPRequestHandler, HTTPServer):
    def __init__(self):
        self.port = 8000
        self.host = 'localhost'

    def start(self):
        server_address = ('', self.port)
        httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
        print("Listening on localhost:"+str(self.port))
        httpd.serve_forever()


def onexit():
    pass

atexit.register(onexit)