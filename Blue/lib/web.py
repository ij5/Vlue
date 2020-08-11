import subprocess
import atexit
import lib.NGINXConf as conf

def start(port=8000):
    c = conf.Conf()
    server = conf.Server()
    
    subprocess.Popen("nginx", shell=True, cwd="nginx")

def onexit():
    subprocess.Popen("nginx -s quit", shell=True, cwd="nginx")
    print("turn off nginx service.")

atexit.register(onexit)