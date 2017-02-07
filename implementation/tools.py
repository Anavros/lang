
from constants import *


def chars(f):
    """
    Iterate over each character in f.
    """
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            yield c


class Processor:
    def __init__(self):
        self.buf = []
        self.tokens = []

    def buffer(self, c):
        self.buf.append(c)

    def add(self, token, ty):
        self.tokens.append(Token(ty, token))

    def chomp(self, ty):
        if self.buf:
            self.tokens.append(Token(ty, ''.join(self.buf)))
            self.buf = []


class Token:
    def __init__(self, t, value):
        if t not in [T_CONSTANT, T_NAME, T_OPERATOR]:
            raise SyntaxError
        self.t = t
        self.value = value

    def __str__(self):
        return "{}{{{}}}".format(self.t, self.value)

    def __repr__(self):
        return str(self)
