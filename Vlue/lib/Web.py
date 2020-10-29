import subprocess
import atexit
import lib.NGINXConf as conf
import platform
import flask
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class Web(BaseHTTPRequestHandler):
    def __init__(self):
        self.port = 8000;
        self.host = 'localhost'

    def _send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-headers", "x-api-key, Content-Type")

    def _send_dict_resounse(self, d):
        self.wfile(bytes(json.dumps(d), "utf8"))

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.send_headers()

    def start(self):
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