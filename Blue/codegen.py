result = ""

class BaseNode():
    def __init__(self):
        pass

class Statement(BaseNode):
    def __init__(self):
        pass

class Declaration(Statement):
    def __init__(self, variable_name, variable_value):
        self.variable_name = variable_name
        self.variable_value = variable_value

class If(BaseNode):
    def __init__(self):
        pass
    def write(self):
        result.append()