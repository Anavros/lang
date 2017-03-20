
from lang.interpreter import executor
from lang.parser.lexer import lexer
from lang.parser.yacker import yacker
from lang.objects import Program


def ast(source):
    lexer.input(source)
    root = yacker.parse(source, lexer)
    # Hacky, but I don't know how to mess with ply.
    # It's too magic.
    if root is None:
        return Program([])
    else:
        return root


def run(root):
    return executor.start(root)
