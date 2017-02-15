
from forms import assignment, variable, parameter, parameterlist
from forms import functiondef, statement, argument, argumentlist
from forms import functioncall, program
import yacker


class Program:
    def __init__(self, statements):
        self.statements = statements
    def __str__(self):
        return program.standard(self)


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
        #return functiondef.standard(self)
        return functiondef.mathematical(self)


class Param:
    def __init__(self, name, type, mut=False, option=False, default=None):
        self.name = name
        self.type = type
        self.mut = mut
        self.option = option
        self.default = default
    def __str__(self):
        #return parameter.standard(self)
        return parameter.mathematical(self)


class Params:
    def __init__(self, params):
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


class FnCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __str__(self):
        return functioncall.standard(self)


class Arg:
    def __init__(self, value, key=None, mut=False, option=False):
        self.value = value
        self.key = key
        self.mut = mut
        self.option = option
    def __str__(self):
        return argument.standard(self)


class Args:
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return argumentlist.standard(self)


lines = [
    St(Assign(Var('x'), 10)),
    Param('str', 'String', option=True),
    Params([Param('n', 'Number'), Param('e', 'Number')]),
    St(FnDef('pow', Params([
        Param('n', 'Number'), Param('e', 'Number')]), 'Number')),
    St(Assign(Var('n'), FnCall('pow', Args(Arg(16), Arg(2))))),
]


def main():
    for element in lines:
        print(element)


def read(path):
    with open(path, 'r') as f:
        source = f.read()
    program = yacker.run(source)
    print(program)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        read(sys.argv[1])
    else:
        main()
