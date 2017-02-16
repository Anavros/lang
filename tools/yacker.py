
from ply import yacc
from lexer import tokens, lexer as lx
from syntax import *


def p_program(p):
    """ program : program line """
    p[0] = p[1]
    p[0].statements.append(p[2])

def p_program_terminal(p):
    """ program : line """
    p[0] = Program([p[1]])

def p_line(p):
    """ line : statement SEMICOLON """
    p[0] = St(p[1])

def p_statement(p):
    """
    statement : function_call
              | function block
              | structure
              | definition
              | mutation
    """
    p[0] = p[1]

def p_definition(p):
    """ definition : lside ASSIGN rside """
    p[0] = Def(p[1], p[3])


def p_mutation(p):
    """ mutation : lside MUTATE rside """
    p[0] = Mut(p[1], p[3])

def p_lside(p):
    """
    lside : NAME
    """
    p[0] = p[1]

def p_rside(p):
    """
    rside : value
          | group
    """
    p[0] = p[1]


# Right-Sides
def p_value(p):
    """
    value : NAME
          | STRING
          | NUMERAL
    """
    p[0] = p[1]

def p_group(p):
    """ group : LPAREN argument_list RPAREN """
    p[0] = p[2]

def p_block(p):
    """ block : LBRACE RBRACE """
    p[0] = "{ }"


# Calls
def p_function_call(p):
    """ function_call : NAME LPAREN argument_list RPAREN """
    p[0] = FnCall(p[1], p[3])

def p_function_call_empty(p):
    """ function_call : NAME LPAREN RPAREN """
    p[0] = FnCall(p[1], Args([]))


# Function Definitions
def p_function_nothing(p):
    """ function : NAME NAME LPAREN RPAREN """
    p[0] = FnDef(p[2], Params([]))

def p_function_no_parameters(p):
    """ function : NAME NAME LPAREN RPAREN NAME NAME """
    p[0] = FnDef(p[2], p[6])

def p_function_no_return(p):
    """ function : NAME NAME LPAREN parameter_list RPAREN """
    p[0] = FnDef(p[2], p[4])

def p_function(p):
    """ function : NAME NAME LPAREN parameter_list RPAREN NAME NAME """
    p[0] = FnDef(p[2], p[4], p[7])


# Structure Definitions
def p_structure_parameterized(p):
    """ structure : NAME NAME LBRACK type_parameter_list RBRACK ASSIGN LPAREN parameter_list RPAREN"""
    p[0] = StrDef(p[2], p[8], generics=p[4])

def p_structure(p):
    """ structure : NAME NAME ASSIGN LPAREN parameter_list RPAREN"""
    p[0] = StrDef(p[2], p[5])


# Type Parameters
def p_type_parameter(p):
    """ type_parameter : NAME """
    p[0] = TpParam(p[1])

def p_type_parameter_list(p):
    """ type_parameter_list : type_parameter_list COMMA type_parameter """
    p[0] = p[1]
    p[0].params.append(p[3])

def p_type_parameter_list_terminal(p):
    """ type_parameter_list : type_parameter """
    p[0] = TpParams([p[1]])


# Parameters
def p_parameter(p):
    """ parameter : NAME NAME """
    p[0] = Param(p[2], p[1])

def p_parameter_list(p):
    """ parameter_list : parameter_list COMMA parameter """
    p[0] = p[1]
    p[0].params.append(p[3])

def p_parameter_list_terminal(p):
    """ parameter_list : parameter """
    p[0] = Params([p[1]])


# Arguments
def p_argument(p):
    """ argument : value """
    p[0] = Arg(p[1])

def p_argument_kw(p):
    """ argument : NAME ASSIGN value """
    p[0] = Arg(p[3], key=p[1])

def p_argument_list(p):
    """ argument_list : argument_list COMMA argument """
    p[0] = p[1]
    p[0].args.append(p[3])

def p_argument_list_terminal(p):
    """ argument_list : argument """
    p[0] = Args([p[1]])


def p_error(p):
    print("Syntax error:", p)

parser = yacc.yacc()

def run(source):
    return parser.parse(source, lx)
