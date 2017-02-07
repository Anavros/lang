
from tools import *
from constants import *
import op


def break_into_statements(f):
    buf = ""
    statements = []
    for c in chars(f):
        if c == STATEMENT:
            statements.append(buf)
            buf = ""
        elif c in WHITESPACE:
            buf += ' '
        else:
            buf += c
    return statements


def break_into_tokens(statement):
    sts = Processor()
    #opstack = []
    quoted = False
    for c in statement:
        if quoted:
            if c == '"':
                quoted = False
                sts.chomp(T_CONSTANT)
            else:
                sts.buffer(c)
        else:
            if c == '"':
                sts.chomp(T_NAME)
                quoted = True
            elif c in KEYWORD:
                sts.buffer(c)
            elif c in WHITESPACE:
                pass
            else:
                sts.chomp(T_NAME)
                sts.add(c, T_OPERATOR)
    sts.chomp(T_OPERATOR)  # what to put here?
    return sts.tokens


def extract_functions(tokens):
    funcs = []
    lastkw = ""
    for t in tokens:
        if values.is_keyword(t):
            lastkw = t
        elif t == LPAREN:
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
        if t.t == T_NAME and not func:
            func = t.value
        elif t.t == T_NAME or t.t == T_CONSTANT:
            args.append(t)
        elif t.t == T_OPERATOR:
            if t.value == LPAREN:
                parens += 1
            elif t.value == RPAREN:
                parens -= 1
            elif t.value == COMMA:
                pass
    return func, args


def execute(operations):
    state = {}
    for f, args in operations:
        op.do(f, args, state)


def main(args):
    f = open(args.filename)
    ments = break_into_statements(f)
    f.close()
    exprs = [break_into_tokens(s) for s in ments]
    mpped = list(map(match_functions_with_arguments, exprs))
    #for e in exprs:
    #    print(e)
    for m in mpped:
        print(m)
    execute(mpped)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    main(parser.parse_args())
