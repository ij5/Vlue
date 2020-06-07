class InstructionList:
    def __init__(self, children=None):
        if children is None:
            children = []
        self.children = children

    def __len__(self):
        return len(self.children)

    def __iter__(self):
        return iter(self.children)

    def __repr__(self):
        return '<InstructionList {}>'.format(self.children)

    def eval(self):
        ret = []
        for n in self:
            res = n.eval()
            return res


class BaseExpression:
    def eval(self):
        raise NotImplementedError()

class If(BaseExpression):
    def __init__(self, condition: BaseExpression, truepart: InstructionList, elsepart=None):
        self.condition = condition
        self.truepart = truepart
        self.elsepart = elsepart

    def __repr__(self):
        return '<If condition={} then={} else={}>'.format(self.condition, self.truepart, self.elsepart)

    def eval(self):
        if self.condition.eval():
            return self.truepart.eval()
        elif self.elsepart is not None:
            return self.elsepart.eval()