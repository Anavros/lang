

from lang.interpreter import storage


def assign(name, value):
    if name in storage.variables.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        storage.variables[name] = value
        print("Set '{}' to '{}'.".format(name, value))


def mutate(name, value):
    if name in storage.variables.keys():
        storage.variables[name] = value
        print("Mutate '{}' to '{}'.".format(name, value))
    else:
        print("Variable '{}' does not exist.")


def create_new_function(name, block):
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
