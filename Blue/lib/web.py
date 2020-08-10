from http import server
import subprocess
import os

def start(port=8000):
    ex ="cd {}".format(os.path.join(os.path.dirname(os.path.abspath(__file__)), "server"))
    print(ex)
    subprocess.Popen(ex).communicate()
    print(ex)
    # result = subprocess.Popen("dir").communicate()
    # print(result)