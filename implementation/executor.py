
import objects


def run(program):
    dump(program)
    execute(program)


def execute(program):
    for o in program.statements:
        if isinstance(o, objects.Program):
            execute(o)
        elif isinstance(o, objects.Call):
            call(o)
        else:
            print("Unknown operation type:", o)


def dump(program):
    for o in program.statements:
        print(o)
    print("\nExecuting...\n")


def call(c):
    global ops, functions
    try:
        functions[c.function.name](c.args)
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


def mutate(args):
    global variables
    name, value = args
    name, value = name.value, value.value
    if name in variables.keys():
        variables[name] = value
        print("Mutate '{}' to '{}'.".format(name, value))
    else:
        print("Variable '{}' does not exist.")


def output(arglist):
    print(*_convert(arglist))


def noop(_):
    print("Noop noop!")


# Only accepts a name and no arguments right now.
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
    'assign': assign,
    'mutate': mutate,
}


variables = {
}
