from http import server
import subprocess
import os
import atexit

def start(port=8000):
    subprocess.Popen("nginx", shell=True, cwd="nginx")

def onexit():
    subprocess.Popen("nginx -s quit", shell=True, cwd="nginx")
    print("turn off nginx service.")

atexit.register(onexit)