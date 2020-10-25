import subprocess
import atexit
import lib.NGINXConf as conf
import platform
import flask

class Web:
    def __init__():
        self.port = 8000;
        self.host = 'localhost'
    def start():
        if(platform.system()=='Windows'):
            c = conf.Conf()
            server = conf.Server()
            server.add(
                conf.Key('listen', '80'),
                conf.Key('listen', '[::]:80'),
                conf.Comment("Hello World!"),
                conf.Key('server_name', self.host),
                conf.Key('include', '../security.conf'),

            )
            subprocess.Popen("nginx.exe", shell=True, cwd="nginx")
        elif(platform.system()=='Linux'):
            c = conf.Conf()
            server = conf.Server()
            server.add(
                conf.Key('listen', '80'),
                conf.Key('listen', '[::]:80'),
                conf.Comment("Hello World!"),
                conf.Key('server_name', self.host),
                conf.Key('include', '/etc/nginx/security.conf'),
                conf.Location(
                    '/',
                    conf.Key('include', '/etc/nginx/python_uwsgi.conf'),
            ),
            
    def start_dev(port=8000, debug=True):
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