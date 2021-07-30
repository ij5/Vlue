from Elementary import ElementaryParser
from Advanced import AdvancedParser
from astor import code_gen
import ast
import time

parser = ElementaryParser()

while(True):
    data = input(">>> ")
    startTime = time.time()
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
        try:
            result = code_gen.to_source(result.VALUE)
            exec(result)
        except Exception as e:
            raise e