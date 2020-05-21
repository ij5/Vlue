import sys
import re

def lex(character):
    IDENTIFIER = re.compile("[a-zA-Z_]+")
    PYTHON = re.compile('`[^`]*`')
    STRING = re.compile('\'[^\']+\'')
    if(IDENTIFIER.match(character)):
        return "IDENTIFIER"
    elif(PYTHON.match(character)):
        return "PYTHON"
    elif(STRING.match(character)):
        return "STRING"
    else:
        return "ERROR"

