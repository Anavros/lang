

TYPE_NUM = "Num"


class Function:
    def __init__(self, name):
        self.name = name
        self.return_type = None
        self.parameters = None
        self.code = None

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
