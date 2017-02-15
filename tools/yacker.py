
from ply import yacc
from lexer import tokens, lexer as lx
from syntax import *


def p_program(p):
    """
    program : program statement
    """
    p[0] = p[1]
    p[0].statements.append(p[2])


def p_program_terminal(p):
    """
    program : statement
    """
    p[0] = Program([p[1]])


def p_statement(p):
    """
    statement : function_call SEMICOLON
              | assignment SEMICOLON
              | function_def SEMICOLON
    """
    p[0] = St(p[1])


def p_function_call(p):
    """
    function_call : NAME LPAREN argument_list RPAREN
    """
    p[0] = FnCall(p[1], p[3])


def p_argument(p):
    """
    argument : value
    """
    p[0] = Arg(p[1])


def p_argument_list(p):
    """
    argument_list : argument_list COMMA argument
    """
    p[0] = p[1]
    p[0].append(p[3])


def p_argument_list_terminal(p):
    """
    argument_list : argument
    """
    p[0] = Args(p[1])


def p_function_def_nothing(p):
    """
    function_def : NAME NAME LPAREN RPAREN
    """
    p[0] = FnDef(p[2], [])


def p_function_def_no_parameters(p):
    """
    function_def : NAME NAME LPAREN RPAREN NAME NAME
    """
    p[0] = FnDef(p[2], p[6])


def p_function_def_no_return(p):
    """
    function_def : NAME NAME LPAREN parameter_list RPAREN
    """
    p[0] = FnDef(p[2], p[4])


def p_function_def(p):
    """
    function_def : NAME NAME LPAREN parameter_list RPAREN NAME NAME
    """
    p[0] = FnDef(p[2], p[4], p[7])


def p_parameter(p):
    """
    parameter : NAME NAME
    """
    p[0] = Param(p[2], p[1])


def p_parameter_list(p):
    """
    parameter_list : parameter_list COMMA parameter
    """
    p[0] = p[1]
    p[0].params.append(p[3])


def p_parameter_list_terminal(p):
    """
    parameter_list : parameter
    """
    p[0] = Params([p[1]])


def p_assignment(p):
    """
    assignment : variable ASSIGN value
    """
    p[0] = Assign(p[1], p[3])


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
    p[0] = Var(p[1])


def p_constant(p):
    """
    constant : STRING
             | NUMERAL
    """
    p[0] = p[1]


def p_error(p):
    print("Syntax error:", p)


parser = yacc.yacc()

def run(source):
    return parser.parse(source, lx)
