
import objects


def run(program):
    dump(program)
    execute(program)


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
                # return retval  # ?
        else:
            print("Unknown operation type:", o)
    return []


def evaluate_all(args):
    return list(map(evaluate, args))

def evaluate(expr):
    global variables
    # expr could be a constant, a variable, or a call.
    # or a block I guess.
    if isinstance(expr, objects.Constant):
        return expr.value
    elif isinstance(expr, objects.Variable):
        try:
            return variables[expr.name]
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
    global operations, functions
    if name in operations.keys():
        operations[name](args)
    elif name in functions.keys():
        subprogram = functions[name]
        print("Executing subprogram.")
        return execute(subprogram)
    else:
        print("Function '{}' is not defined.".format(name))
    return []


def assign(args):
    global variables
    name, value = args
    if name in variables.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        variables[name] = value
        print("Set '{}' to '{}'.".format(name, value))


def mutate(args):
    global variables
    name, value = args
    if name in variables.keys():
        variables[name] = value
        print("Mutate '{}' to '{}'.".format(name, value))
    else:
        print("Variable '{}' does not exist.")


def output(arglist):
    print(*arglist)


def noop(_):
    print("...")


def create_new_function(args):
    global functions
    if len(args) != 2:
        print("Bad arguments to function()!")
        return
    name, block = args
    if name in functions.keys():
        print("Function '{}' already exists.".format(name))
    else:
        functions[name] = block
        print("Created new function:", name)


# Built-in functions.
operations = {
    'print': output,
    'function': create_new_function,
    'assign': assign,
    'mutate': mutate,
}
functions = { }
variables = { }
