from http import server
import subprocess
import os

def start(port=8000):
    subprocess.Popen("nginx", shell=True, cwd="nginx")
    