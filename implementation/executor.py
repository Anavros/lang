
import objects


def run(program):
    dump(program)
    execute(program)


def execute(program):
    for o in program.statements:
        if isinstance(o, objects.Program):
            execute(o)
        elif isinstance(o, objects.Call):
            # TODO? Remove hard-coded return?
            # Should return be a function too?
            if o.function.name == 'return':
                return
            else:
                call(o)
        else:
            print("Unknown operation type:", o)


def dump(program):
    for o in program.statements:
        print(o)
    print("\nExecuting...\n")


def call(c):
    global operations, functions
    name = c.function.name
    args = c.args
    if name in operations.keys():
        operations[name](args)
    elif name in functions.keys():
        #print("Calling '{}'...".format(name))
        execute(functions[name])
    else:
        print("Function '{}' is not defined.".format(name))


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
    print("...")


def ret(_):
    print("Should be returning...")


def create_new_function(args):
    global functions
    if len(args) != 2:
        print("Bad arguments to function()!")
        return
    constant, block = args
    name = constant.value
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
    'return': ret,
}
functions = { }
variables = { }
