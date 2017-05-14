
# from functools import partial

from lang.objects import *
from lang.interpreter import operations, tools

debug = tools.debug
tools.DEBUG = True


def start(program):
    retval = evaluate(program, create_global_scope())
    print("Program finished with value:", retval)
    return retval


def create_global_scope():
    return(
    { 'print' : operations.print_
    , 'assign' : operations.assign
    , 'mutate' : operations.mutate
    , 'function' : operations.create_new_function
    , 'sum' : operations.sum_
    , 'difference' : operations.difference
    , 'product' : operations.product
    , 'quotient' : operations.quotient
    , 'execute' : evaluate
    })


# Convert language objects into python values.
# Returns a list of (key, value) pairs.
def evaluate(expr, scope):
    if not isinstance(expr, Lang):
        return expr

    elif type(expr) is Program:
        for statement in expr.statements:
            name = statement.name
            args = statement.args
            if name == 'return':
                return enumerate_args(evaluate(args, scope))
            else:
                # Don't return until return.
                retval = do(name, evaluate(args, scope), scope)

    elif type(expr) is Call:
        name = expr.name
        args = expr.args
        if name == 'return':
            print("Calling return as expression? Probably bad.")
            return evaluate(args, scope)
        else:
            # If something is called as an expression,
            # we do need to return that value.
            retval = do(name, evaluate(args, scope), scope)
            return retval

    elif type(expr) is Tuple:
        bindings = []
        for value in expr.values:
            bindings.append(evaluate(value, scope))
        return bindings

    elif type(expr) is Value:
        if expr.val is None:
            # Variable lookup.
            if expr.key in scope.keys():
                #return expr.key, scope[expr.key]
                # Variables aren't necessarily kwargs.
                # If you return expr.key, it will be treated like
                # a kwarg.
                return None, scope[expr.key]
            else:
                print("Lookup Error:", expr, type(expr))
                return None, None
        else:
            return expr.key, evaluate(expr.val, scope)

    else:
        print("Evaluation Error:", expr, type(expr))
        return []


def enumerate_args(args):
    """
    Change the keys of all unnamed args into their positions.
    Named args are kept the same.
    """
    result = []
    for i, argument in enumerate(args):
        k, v = argument
        if k is None:
            k = i  # positional args have no keyword
        result.append((k, v))
    return result


def convert_args(args):
    """
    Convert args from a list of (key, value) pairs to a dict.
    """
    return {k:v for k, v in args}


def do(name, args, scope):
    """
    Call a lang function. Provides global and local scopes.
    """
    if name in scope.keys():
        subscope = convert_args(enumerate_args(args));
        # Mutates scope in place.
        return scope[name](scope, subscope)
    else:
        print("Function Lookup Error:", name)
        return []
