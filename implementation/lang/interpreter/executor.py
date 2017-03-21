
from functools import partial

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


def dump(program):
    for o in program.statements:
        print(o)


# Convert language objects into python values.
def evaluate(expr, scope):
    if isinstance(expr, Value):
        # if expr.val is None ... do name lookup
        return expr.key, evaluate(expr.val, scope)

    elif isinstance(expr, Tuple):
        bindings = {}
        for k, v in expr.values.items():
            bindings[k] = evaluate(v, scope)
        return bindings

    elif isinstance(expr, Call):
        name = expr.function.name
        args = expr.args
        if name == 'return':
            print(args)
            return evaluate(args, scope)
        else:
            return call(name, evaluate(args, scope), scope)

    elif isinstance(expr, Program):
        return [evaluate(s, scope) for s in expr.statements]

    else:
        print("Evaluation Error:", expr, type(expr))
        return {}


def call(name, args, scope):
    if name in scope.keys():
        subscope = scope.copy();
        subscope.update(args);
        return scope[name](subscope)
    else:
        print("Function '{}' is not defined.".format(name))
        return {}
