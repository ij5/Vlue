import subprocess
import atexit
import lib.NGINXConf as conf
import os

def start(port=8000):
    c = conf.Conf()
    server = conf.Server()
    server.add(
        conf.Key('listen', '80'),
        conf.Comment("Hello World!"),
        conf.Key('server_name', '127.0.0.1'),
        conf.Key('root', )
    )
    subprocess.Popen("nginx", shell=True, cwd="nginx")

def onexit():
    subprocess.Popen("nginx -s quit", shell=True, cwd="nginx")
    print("turn off nginx service.")

atexit.register(onexit)