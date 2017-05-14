
from ply import yacc
from lang.objects import *
from lang.parser import runtime
from lang.parser.lexer import tokens


def p_program(p):
    """
    program : program statement
    """
    p[0] = p[2]


def p_program_end(p):
    """
    program : return SEMICOLON
    """
    p[0] = p[1]


def p_statement(p):
    """
    statement : call SEMICOLON
    statement : definition SEMICOLON
    """
    p[0] = p[1]


def p_return(p):
    """
    return : RETURN value
    """
    p[0] = p[2]


def p_definition(p):
    """
    definition : DEFINE NAME value
    """
    runtime.add_variable(p[2], p[3])


def p_function_definition(p):
    """
    definition : DEFINE NAME tuple block
    """
    runtime.add_variable(p[1], 0) # TODO


def p_call(p):
    """
    call : NAME tuple
    """
    p[0] = runtime.evaluate_function(p[1], p[2])


def p_tuple(p):
    """
    tuple : LPAREN arguments RPAREN
    """
    p[0] = p[2]


def p_tuple_empty(p):
    """
    tuple : LPAREN RPAREN
    """
    p[0] = ()


def p_arguments_single(p):
    """
    arguments : arg
    """
    p[0] = [p[1]]


def p_arguments_list(p):
    """
    arguments : arguments COMMA arg
    """
    p[0] = [p[3]]
    p[0] = p[1] + p[0]  # prepend so they're in order


def p_arg(p):
    """
    arg : positional_value
        | named_value
        | variable
    """
    p[0] = p[1]

def p_named_value(p):
    """
    named_value : NAME ASSIGN value
    """
    p[0] = Value(p[1], p[3])


def p_positional_value(p):
    """
    positional_value : value
    """
    p[0] = Value(None, p[1])

def p_value(p):
    """
    value : constant
          | block
          | call
          | tuple
    """
    p[0] = p[1]

def p_variable(p):
    """
    variable : NAME
    """
    p[0] = runtime.evaluate_variable(p[1])


def p_constant(p):
    """
    constant : STRING
             | NUMERAL
    """
    p[0] = p[1]


def p_block(p):
    """
    block : LBRACE program RBRACE
    """
    p[0] = p[2]


def p_error(p):
    print("Syntax error.", p)


yacker = yacc.yacc()
