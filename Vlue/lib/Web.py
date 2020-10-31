import atexit
from http.server import CGIHTTPRequestHandler

cgi = CGIHTTPRequestHandler()



def onexit():
    pass

atexit.register(onexit)