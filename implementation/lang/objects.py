

class Result:
    def __init__(self):
        pass


class Lang: pass


class Program(Lang):
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        lines = []
        lines.append("PROGRAM {")
        for st in self.statements:
            lines.append(repr(st))
        lines.append("}")
        return '\n'.join(lines)


class Call(Lang):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def __repr__(self):
        return "CALL({}, {})".format(self.name, self.args)


class Tuple(Lang):
    def __init__(self, values):
        # List of values with keys set to either positions or keywords.
        self.values = values

    def __repr__(self):
        return str(self.values)


class Value(Lang):
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __repr__(self):
        return "({}={})".format(self.key, self.val) 
