from http import server
import subprocess
import os

def _start(port=8000):
    subprocess.Popen("nginx", shell=True, cwd="nginx")

def start(port=8000):
    try:
        _start(port)
    except KeyboardInterrupt:
        subprocess.Popen("nginx -s quit")