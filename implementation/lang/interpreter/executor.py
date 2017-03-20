
from lang import objects

from lang.interpreter import operations, storage


def start(program):
    assign_builtins()
    return execute(program)


def assign_builtins():
    storage.ops['print'] = operations.output
    storage.ops['assign'] = operations.assign
    storage.ops['mutate'] = operations.mutate
    storage.ops['function'] = operations.create_new_function
    storage.ops['sum'] = operations.sum
    storage.ops['difference'] = operations.difference
    storage.ops['product'] = operations.product
    storage.ops['quotient'] = operations.quotient


def dump(program):
    for o in program.statements:
        print(o)
    print("\nExecuting...\n")


def execute(program):
    for o in program.statements:
        if isinstance(o, objects.Program):
            execute(o)
        elif isinstance(o, objects.Call):
            # TODO? Remove hard-coded return?
            # Should return be a function too?
            if o.function.name == 'return':
                return evaluate_all(o.args)
            else:
                retval = call(o) # should this return a value?
                return retval
        else:
            print("Unknown operation type:", o)
    return []


def evaluate_all(args):
    return list(map(evaluate, args))

def evaluate(expr):
    # expr could be a constant, a variable, or a call.
    # or a block I guess.
    if isinstance(expr, objects.Constant):
        return expr.value
    elif isinstance(expr, objects.Variable):
        try:
            return storage.variables[expr.name]
        except KeyError:
            return '?'
    elif isinstance(expr, objects.Call):
        return call(expr)
    elif isinstance(expr, objects.Program):
        return expr
    else:
        print("Can't evaluate '{}'.".format(expr))


def call(o):
    name = o.function.name
    args = evaluate_all(o.args)
    ops = storage.ops
    if name in ops.keys():
        # Do none of the operations have retvals?
        # Actually, here's the problem. Sum has a retval.
        # But it's an operation.
        retval = ops[name](*args)
        print("CALL:", name, "with", args, "returning", retval)
        return [retval]
    elif name in storage.functions.keys():
        subprogram = storage.functions[name]
        print("Executing subprogram.")
        return execute(subprogram)
    else:
        print("Function '{}' is not defined.".format(name))
    return []
