

from lang.interpreter import storage


def assign(args):
    name, value = args
    if name in storage.variables.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        storage.variables[name] = value
        print("Set '{}' to '{}'.".format(name, value))


def mutate(args):
    name, value = args
    if name in storage.variables.keys():
        storage.variables[name] = value
        print("Mutate '{}' to '{}'.".format(name, value))
    else:
        print("Variable '{}' does not exist.")


def output(arglist):
    print(*arglist)


def noop(_):
    print("...")


def create_new_function(args):
    if len(args) != 2:
        print("Bad arguments to function()!")
        return
    name, block = args
    if name in storage.functions.keys():
        print("Function '{}' already exists.".format(name))
    else:
        storage.functions[name] = block
        print("Created new function:", name)


def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

def quotient(a, b):
    return a / b
