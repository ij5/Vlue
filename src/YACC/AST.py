class AST(object):
    nodes = {}

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        argstr = ', '.join(f'{name}={type(values).__name__ if isinstance(values, AST) else repr(values)}'
                           for name, val in zip(self._fields, values))
        return f'{type(self).__name__}({argstr}'

class Statement(AST):
    pass

class Expression(AST):
    pass

class Literal(Expression):
    pass

class DataType(AST):
    pass

class Location(AST):
    pass

class PrintStatement(Statement):
    value: Expression

class IntegerLiteral(Literal):
    value: int

class FloatLiteral(Literal):
    value: float

class StringLiteral(Literal):
    value: str

class BoolLiteral(Literal):
    value: bool

