
from ply import lex

tokens = (
    "RETURN",
    "DEFINE",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "ASSIGN",
    "SEMICOLON",
    "COMMA",
    "COLON",
    "NUMERAL",
    "STRING",
    "NAME",
)


reserved = {
    "return": "RETURN",
    "define": "DEFINE",
}


t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_ASSIGN    = r'='
t_SEMICOLON = r';'
t_COMMA     = r','
t_COLON     = r':'


def t_NAME(t):
    r'[A-Za-z_][A-Za-z_0-9]*'
    if t.value in reserved.keys():
        t.type = reserved[t.value]
    return t
    


def t_NUMERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t


def t_COMMENT(t):
    r'\#.*'


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character: '{}'.".format(t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()


def dump(source):
    lexer.input(source)
    for t in lexer:
        print(t)
