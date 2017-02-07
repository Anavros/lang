
from string import ascii_letters, digits, whitespace
from tools import Processor, chars

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


def main(args):
    f = open(args.filename)
    ments = break_into_statements(f)
    exprs = [break_into_tokens(s) for s in ments]
    funcs = list(map(extract_functions, exprs))
    print(exprs)
    print(funcs)
    f.close()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    main(parser.parse_args())
