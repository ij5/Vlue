import time
from Elementary import ElementaryParser
from Advanced import AdvancedParser
from astor import code_gen
import ast
import re
import os



filename = input("input file name: ")
startTime = time.time()
data = open(filename, 'r', encoding='UTF-8').read()
IS_ADVANCED = False
if(filename[-2:]=='bl'):
    IS_ADVANCED = False
elif(filename[-3:]=='bla'):
    IS_ADVANCED = True
else:
    print("Invalid file format.")
    exit(-1)

if(IS_ADVANCED==True):
    # dt = re.compile("use\s+[a-zA-Z0-9_]+;")
    # libres = dt.findall(data)
    # for lib in libres:
    #     lib = lib[3:-1].strip()
    #     libfile = lib + ".blib"
    #     realpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib", libfile)
    #     if os.path.isfile(realpath):
    #         f.append(open(realpath, 'r', encoding='UTF-8').read())
    #     else:
    #         print("There are no library named " + lib)
    #
    # d = dict(locals(), **globals())
    # for ff in f:
    #     exec(ff, d, d)
    parser = AdvancedParser()
    result = parser.parser.parse(data, debug=0)
    print("============== ABSTRACT SYNTAX TREE ==============")
    print(ast.dump(result.VALUE))
    print()
    result = code_gen.to_source(result.VALUE)
    print("============== PYTHON CODE ==============")
    print(result)
    print()
    print("============== RESULT ==============")
    exec(result)
    print()
    print("Task finished in " + str(time.time() - startTime) + "s")
else:
    parser = ElementaryParser()
    result = parser.parser.parse(data, debug=0, tracking=True)
    if(parser.debug==True):
        print("============== ABSTRACT SYNTAX TREE ==============")
        print(ast.dump(result.VALUE))
        print()
        result = code_gen.to_source(result.VALUE)
        print("============== PYTHON CODE ==============")
        print(result)
        print()
        print("============== RESULT ==============")
        exec(result)
        print()
        print("Task finished in " + str(time.time() - startTime) + "s")
    else:
        result = code_gen.to_source(result.VALUE)
        exec(result)