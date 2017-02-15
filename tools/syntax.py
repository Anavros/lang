
from forms import assignment, variable, call, parameter, parameterlist
from forms import functiondef, statement


class St:
    def __init__(self, body):
        self.body = body
    def __str__(self):
        return statement.standard(self)


class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(self):
        return assignment.standard(self)


class FnDef:
    def __init__(self, name, params, ret=None):
        self.name = name
        self.params = params
        self.ret = ret
    def __str__(self):
        return functiondef.standard(self)


class Param:
    def __init__(self, name, type, mut=False, option=False, default=None):
        self.name = name
        self.type = type
        self.mut = mut
        self.option = option
        self.default = default
    def __str__(self):
        return parameter.standard(self)


class Params:
    def __init__(self, *params):
        self.params = params
    def __str__(self):
        return parameterlist.standard(self)


class Var:
    def __init__(self, name, mut=False, maybe=False):
        self.name = name
        self.mut = mut
        self.maybe = maybe
    def __str__(self):
        return variable.standard(self)


lines = [
    St(Assign(Var('x'), 10)),
    Param('str', 'String', option=True),
    Params(Param('n', 'Number'), Param('e', 'Number')),
    FnDef(
        'pow',
        Params(
            Param('n', 'Number'), Param('e', 'Number')),
        'Number',
    ),
]


def main():
    for element in lines:
        print(element)


if __name__ == '__main__':
    main()
