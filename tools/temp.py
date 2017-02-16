
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
