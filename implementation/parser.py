
from string import ascii_letters, digits, whitespace
from tools import Processor, chars
from op import *

LPAREN = '('
LBRACE = '{'
LBRACK = '['
RPAREN = ')'
RBRACE = '}'
RBRACK = ']'
GROUPS = '({[]})'
DOUBLE_QUOTE = '"'
SINGLE_QUOTE = "'"
STATEMENT = ';'
KEYWORD = ascii_letters + digits
WHITESPACE = whitespace


def break_into_statements(f):
    sts = Processor()
    for c in chars(f):
        if c == STATEMENT:
            sts.chomp()
        elif c in WHITESPACE:
            sts.buffer(' ')
        else:
            sts.buffer(c)
    return sts.tokens


def break_into_tokens(statement):
    sts = Processor()
    for c in statement:
        if c in KEYWORD:
            sts.buffer(c)
        elif c in WHITESPACE:
            pass
        else:
            sts.chomp()
            sts.add(c)
    sts.chomp()
    return sts.tokens


def extract_functions(tokens):
    funcs = []
    lastkw = ""
    for t in tokens:
        if set(t) <= set(KEYWORD):
            lastkw = t
        elif t == '(':
            funcs.append(lastkw+"()")
    return funcs


def extract_assignments(tokens):
    assign = {};
    key = ""
    valtrap = False
    for t in tokens:
        if valtrap:
            assign[key] = t
            valtrap = False
        elif set(t) <= set(KEYWORD):
            key = t
        elif t == '=':
            assign[key] = None
            valtrap = True
    return assign


def match_functions_with_arguments(tokens):
    """
    ['print', '(', ')'] => execute('print', [])
    ['print', '(', '10', ')'] => execute('print', [10])
    ['(', 'print', ')'] => error or expression?
    """
    func = ""
    args = []
    parens = 0
    for t in tokens:
        if set(t) <= set(KEYWORD):
            if parens:
                args.append(t)
            else:
                func = t
        elif t == LPAREN:
            parens += 1
        elif t == RPAREN:
            parens -= 1
    return func, args


def execute(operations):
    for f, args in operations:
        if f == 'print':
            op_print(args)


def main(args):
    f = open(args.filename)
    ments = break_into_statements(f)
    exprs = [break_into_tokens(s) for s in ments]
    #funcs = list(map(extract_functions, exprs))
    #assgn = list(map(extract_assignments, exprs))
    mpped = list(map(match_functions_with_arguments, exprs))
    execute(mpped)
    #print(exprs)
    #print(funcs)
    #print(assgn)
    #print(mpped)
    f.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    main(parser.parse_args())
