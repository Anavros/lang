
from ply import yacc
from lang.objects import *
from lang.parser import runtime
from lang.parser.lexer import tokens


def p_program(p):
    """
    program : program statement
    """
    p[0] = p[1]
    p[0].statements.append(p[2])


def p_program_end(p):
    """
    program : statement
    """
    p[0] = Program([p[1]])


def p_statement(p):
    """
    statement : call SEMICOLON
    """
    p[0] = p[1]


def p_return(p):
    """
    return : RETURN value SEMICOLON
    """
    p[0] = p[2]


def p_call(p):
    """
    call : NAME tuple
    """
    p[0] = runtime.evaluate_function(Call(p[1], p[2]))


def p_tuple(p):
    """
    tuple : LPAREN arguments RPAREN
    """
    bindings = p[2]
    for i, value in enumerate(bindings):
        if value.key is None:
            value.key = i
    p[0] = Tuple(bindings)


def p_tuple_empty(p):
    """
    tuple : LPAREN RPAREN
    """
    p[0] = Tuple([])


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
    p[0] = Value(p[1], None)


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
