

TYPE_NUM = "Num"


class Program:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return "Program {{\n{}\n}}".format(self.statements)


class Call:
    def __init__(self, function, args):
        self.function = function
        self.args = args

    def __repr__(self):
        return "Call({}, {})".format(self.function, self.args)


class Function:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Fn[{}]".format(self.name)


class Constant:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "C[{}]".format(self.value)


class Variable:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "V[{}]".format(self.name)
