import sys

NE = 0

def error(lineno, message, filename=None):
    global NE
    if not filename:
        errormsg = "{}: {}".format(lineno, message)
    else:
        errormsg = "{}: {}: {}".format(filename, lineno, message)

    print(errormsg, file = sys.stderr)
    NE += 1

def errors_reported():
    return NE

def clear_errors():
    global NE
    NE = 0
