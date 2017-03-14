
from ply import yacc
from lexer import tokens
from objects import *


def p_program(p):
    """
    program : program statement
    """
    p[0] = p[1]
    p[0].append(p[2])


def p_program_end(p):
    """
    program : statement
    """
    p[0] = [p[1]]


def p_statement(p):
    """
    statement : call SEMICOLON
    """
    p[0] = p[1]


def p_call(p):
    """
    call : NAME LPAREN arguments RPAREN
    """
    p[0] = (Function(p[1]), p[3])


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
    p[0] = p[1] + p[0]  # prepend so they're in order


def p_value(p):
    """
    value : variable
          | constant
    """
    p[0] = p[1]


def p_variable(p):
    """
    variable : NAME
    """
    p[0] = Variable(p[1])


def p_constant(p):
    """
    constant : STRING
             | NUMERAL
    """
    p[0] = Constant(p[1])


def p_error(p):
    print("Syntax error.")


parser = yacc.yacc()


def run(source, lx):
    return parser.parse(source, lx)
