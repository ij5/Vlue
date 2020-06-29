result = ""

class SourceGenerator():
    def __init__(self):
        pass

class BaseNode():
    def __init__(self):
        pass

class Statement(BaseNode):
    def __init__(self):
        pass

class Expression(BaseNode):
    def __init__(self):
        pass

class VariableDeclaration(Statement):
    def __init__(self, variable_name, variable_value=0):
        if(isinstance(variable_value, int)):
            self.source = 'int {} = {};'.format(variable_name, variable_value)
        if(isinstance(variable_value, float)):
            self.source = 'float {} = {};'.format(variable_name, variable_value)

class FunctionDeclaration(Statement):
    def __init__(self):
        pass



class FunctionCall(Expression):
    def __init__(self):
        pass


class If(Statement):
    def __init__(self):
        pass
    def write(self):
        result.append()