import time
from astor import code_gen
import ast
import sys
import bottle

if(len(sys.argv)==1):
    from Elementary import ElementaryParser
    parser = ElementaryParser()

    while (True):
        data = input(">>> ")
        startTime = time.time()
        result = parser.parser.parse(data, debug=0, tracking=True)
        if (parser.debug == True):
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
            try:
                result = code_gen.to_source(result.VALUE)
                exec(result)
            except Exception as e:
                raise e
elif(len(sys.argv)==2):
    filename = sys.argv[1]
    startTime = time.time()
    data = open(filename, 'r', encoding='UTF-8').read()
    IS_ADVANCED = False
    if(filename[-3:]=='ebl'):
        IS_ADVANCED = True
    elif(filename[-2:]=='bl'):
        IS_ADVANCED = False
    else:
        print("Invalid file format.")
        exit(-1)

    if(IS_ADVANCED==True):
        from HTML import HTMLParser
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
        parser = HTMLParser()
        result = parser.parser.parse(data, debug=0)
        if(parser.debug==True):
            print("============== HTML ==============")
            print(result)
            print()
            print("Task finished in " + str(time.time() - startTime) + "s")
        else:
            result = code_gen.to_source(result.VALUE)
            exec(result)

    else:
        from Elementary import ElementaryParser
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

else:
    print("Too many arguments.")
    exit(-1)