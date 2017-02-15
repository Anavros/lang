
from ply import lex

tokens = (
    "LPAREN",
    "RPAREN",
    "ASSIGN",
    "SEMICOLON",
    "COMMA",
    "COLON",
    "NUMERAL",
    "STRING",
    "NAME",
)

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_ASSIGN    = r'='
t_SEMICOLON = r';'
t_COMMA     = r','
t_COLON     = r':'
t_STRING    = r'".*"'
t_NAME      = r'[A-Za-z_][A-Za-z_0-9]*'

def t_NUMERAL(t):
    r'\d+'
    t.value = int(t.value)
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

def run(source):
    lexer.input(source)
    for t in lexer:
        print(t)
