import subprocess
import atexit
import lib.NGINXConf as conf
import platform
import flask
from http.server import HTTPServer, BaseHTTPRequestHandler

class Web(BaseHTTPRequestHandler):
    def __init__():
        self.port = 8000;
        self.host = 'localhost'
        
    def start():
        pass
            
    def start_dev(self, port=8000, debug=True):
        app = flask.Flask(__name__)
        app.run(debug=debug,)

def onexit():
    if(platform.system()=="Windows"):
        #subprocess.Popen("pkill gunicorn")
        subprocess.Popen("nginx -s quit", shell=True, cwd="nginx")
    elif(platform.system()=="Linux"):
        subprocess.Popen("nginx -s quit", shell=True)
    print("turn off nginx service.")

atexit.register(onexit)