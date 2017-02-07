
from ply import yacc
from lexer import tokens


def p_program(p):
    """
    program : program SEMICOLON statement
    """
    p[0] = p[3]
    p[0].extend(p[1])


def p_program_end(p):
    """
    program : statement SEMICOLON
    """
    p[0] = [p[1]]


def p_statement(p):
    """
    statement : call
              | assignment
    """
    p[0] = p[1]


def p_call(p):
    """
    call : NAME LPAREN arguments RPAREN
    """
    #p[0] = return value of p[1]
    p[0] = p[1], p[3]


def p_assignment(p):
    """
    assignment : NAME ASSIGN value
    """
    p[0] = "{} = {}".format(p[1], p[3])


def p_arguments(p):
    """
    arguments : value
    """
    p[0] = [p[1]]


def p_arguments_list(p):
    """
    arguments : arguments COMMA value
    """
    p[0] = [p[3]]
    p[0].extend(p[1])


def p_value(p):
    """
    value : NAME
          | STRING
          | NUMERAL
    """
    p[0] = p[1]


def p_error(p):
    print("Syntax error.")


parser = yacc.yacc()


def run(source, lx):
    return parser.parse(source, lx)
