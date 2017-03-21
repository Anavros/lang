

def assign(storage, name, value):
    if name in storage.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        storage[name] = value
        print("Set '{}' to '{}'.".format(name, value))


def mutate(storage, name, value):
    if name in storage.keys():
        storage[name] = value
        print("Mutate '{}' to '{}'.".format(name, value))
    else:
        print("Variable '{}' does not exist.")


def create_new_function(scope, name, args, block):
    if name in scope.keys():
        print("Function '{}' already exists.".format(name))
    else:
        def f(*args):
            return scope['execute'](block, scope)
        scope[name] = f
        print("Created new function:", name)


def print_(scope, *args):
    print(*args)


def sum_(_, a, b):
    return a + b

def difference(_, a, b):
    return a - b

def product(_, a, b):
    return a * b

def quotient(_, a, b):
    return a / b
