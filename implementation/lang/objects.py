

class Result:
    def __init__(self):
        pass


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
        self.code = "TODO!"

    def __repr__(self):
        return "Fn|{}|".format(self.name)


class Tuple:
    def __init__(self, values):
        # List of values with keys set to either positions or keywords.
        self.values = values

    def __repr__(self):
        return str(self.values)


class Value:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return "{}={}".format(self.key, self.val) 
