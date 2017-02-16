
import yacker


class Program:
    def __init__(self, statements):
        self.statements = statements
    def __str__(self):
        return '\n'.join(map(str, self.statements))


class St:
    def __init__(self, body):
        self.body = body
    def __str__(s):
        return str(s.body) + ';'


# Double 'def' Def+FnDef
class Def:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(a):
        return "def {name} = {value}".format(**a.__dict__)
        #return "{name} = {value}".format(**a.__dict__)


class Mut:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def __str__(a):
        return "mut {name} = {value}".format(**a.__dict__)
        #return "{name} := {value}".format(**a.__dict__)



class FnDef:
    def __init__(self, name, params, ret=None):
        self.name = name
        self.params = params
        self.ret = ret
    def __str__(s):
        base = "def {name}{params}"
        if s.ret:
            base += " returns {ret}"
        return base.format(**s.__dict__)


class Param:
    def __init__(self, name, type, mut=False, option=False, default=None):
        self.name = name
        self.type = type
        self.mut = mut
        self.option = option
        self.default = default
    def __str__(s):
        return "{type} {name}".format(**s.__dict__)
        #return "{name}:{type}".format(**s.__dict__)


class Params:
    def __init__(self, params):
        self.params = params
    def __str__(self):
        return '('+', '.join(map(str, self.params))+')'


class StrDef:
    def __init__(self, name, params, generics=None):
        self.name = name
        self.params = params
        self.generics = generics
    def __str__(s):
        return "{name}{generics} = {params}".format(**s.__dict__)


class TpParam:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name


class TpParams:
    def __init__(self, params):
        self.params = params
    def __str__(self):
        return '['+', '.join(map(str, self.params))+']'


class FnCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __str__(s):
        return "{name}{args}".format(**s.__dict__)


class Arg:
    def __init__(self, value, key=None, mut=False, option=False):
        self.value = value
        self.key = key
        self.mut = mut
        self.option = option
    def __str__(a):
        if a.key:
            base = "{key} = {value}"
        else:
            base = "{value}"
        if a.option:
            base += '?'
        if a.mut:
            base += '!'
        return base.format(**a.__dict__)


class Args:
    def __init__(self, args):
        self.args = args
    def __str__(l):
        return '('+', '.join(map(str, l.args))+')'


class Var:
    def __init__(self, name, mut=False, maybe=False):
        self.name = name
        self.mut = mut
        self.maybe = maybe
    def __str__(self):
        return self.name


lines = [
    FnDef("panic", Params([]))
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
