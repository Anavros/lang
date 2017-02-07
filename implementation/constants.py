
from string import ascii_letters, digits, whitespace

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
COMMA = ','
KEYWORD = ascii_letters + digits
WHITESPACE = whitespace

T_NAME = "Name"
T_OPERATOR = "Operator"
T_CONSTANT = "Constant"
