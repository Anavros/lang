
from functools import partial

from lang import objects

from lang.interpreter import operations, tools

debug = tools.debug

def start(program):
    tools.DEBUG = False
    retval = execute(program, create_global_scope())
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
    , 'execute' : execute
    })


def dump(program):
    for o in program.statements:
        print(o)


def execute(program, scope):
    for o in program.statements:
        if isinstance(o, objects.Program):
            return execute(o, scope)
        elif isinstance(o, objects.Call):
            if o.function.name == 'return':
                return evaluate_all(o.args, scope)
            else:
                retval = call(o, scope) # should this return a value?
                # If a function returns in the middle of the program,
                # the whole program stops.
                #return retval
        else:
            print("Unknown operation type:", o)
    return []


def evaluate_all(args, scope):
    return [evaluate(e, scope) for e in args]

def evaluate(expr, scope):
    # expr could be a constant, a variable, or a call.
    # or a block I guess.
    # or a tuple
    if isinstance(expr, objects.Constant):
        return expr.value
    elif isinstance(expr, objects.Variable):
        try:
            return scope[expr.name]
        except KeyError:
            return '?'
    elif isinstance(expr, objects.Call):
        return call(expr, scope)
    elif isinstance(expr, objects.Program):
        return expr
    elif isinstance(expr, objects.Tuple):
        return evaluate_all(expr.values, scope)
    else:
        print("Can't evaluate '{}'.".format(expr))


def call(o, scope):
    name = o.function.name
    args = evaluate_all(o.args, scope)
    if name in scope.keys():
        return scope[name](scope, *args)
    else:
        print("Function '{}' is not defined.".format(name))
        return []
