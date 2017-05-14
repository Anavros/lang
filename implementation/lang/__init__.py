
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


def evaluate(source):
    lexer.input(source)
    return yacker.parse(source, lexer)


def run(source):
    return executor.start(ast(source))


def dump_tokens(source):
    lexer.input(source)
    for token in lexer:
        print(token)


def dump_ast(source):
    print(ast(source))
