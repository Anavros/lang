
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
                return evaluate(args, scope)
            else:
                # Don't return until return.
                do(name, evaluate(args, scope), scope)

    elif type(expr) is Call:
        name = expr.name
        args = expr.args
        if name == 'return':
            return evaluate(args, scope)
        else:
            # If something is called as an expression,
            # we do need to return that value.
            return do(name, evaluate(args, scope), scope)

    elif type(expr) is Tuple:
        bindings = []
        for value in expr.values:
            bindings.append((value.key, evaluate(value.val, scope)))
        return bindings

    elif type(expr) is Value:
        # if expr.val is None ... do name lookup
        return expr.key, evaluate(expr.val, scope)

    else:
        print("Evaluation Error:", expr, type(expr))
        return []


def do(name, args, scope):
    if name in scope.keys():
        subscope = scope.copy();
        subscope.update(args);
        # return scope?
        return scope[name](subscope)
    else:
        print("Function '{}' is not defined.".format(name))
        return []
