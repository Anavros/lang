
import objects


def run(operations):
    global ops
    dump(operations)
    for o in operations:
        call(o)


def dump(operations):
    for o in operations:
        print(o)
    print("\nExecuting...\n")


def call(args):
    global ops, functions
    f, args = args
    try:
        functions[f.name](args)
    except KeyError:
        print("Unknown function:", f.name)


def _convert(args):
    global variables
    values = []
    for a in args:
        if isinstance(a, objects.Variable):
            try:
                value = variables[a.name]
            except KeyError:
                value = '?'
            values.append(value)
        elif isinstance(a, objects.Constant):
            values.append(a.value)
    return values


def assign(args):
    global variables
    name, value = args
    name, value = name.value, value.value
    if name in variables.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        variables[name] = value
        print("Set '{}' to '{}'.".format(name, value))


def output(arglist):
    print(*_convert(arglist))


def noop(_):
    print("Noop noop!")


# Only accepts a name and no arguments right now.
# Which is bad because the parser doesn't recognize empty params.
def create_new_function(args):
    global functions
    if len(args) != 1:
        print("Bad arguments to function()!")
        return
    name = args[0].value
    if name in functions.keys():
        print("Function '{}' already exists.".format(name))
    else:
        functions[name] = noop
        print("Created new function:", name)


ops = {
    'CALL': call,
}


functions = {
    'print': output,
    'function': create_new_function,
    'assign': assign
}


variables = {
}
