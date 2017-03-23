

# Create a binding in the global namespace.
# Mutates global scope.
def assign(scope, local):
    name  = local[0]
    value = local[1]
    if name in scope.keys():
        print("Variable '{}' already exists!".format(name))
    else:
        scope[name] = value
        print("Set '{}' to '{}'.".format(name, value))
    return []


def mutate(scope, local):
    name = local[0]
    newvalue = local[1]
    if name in scope.keys():
        scope[name] = newvalue
        print("Mutate '{}' to '{}'.".format(name, newvalue))
    else:
        print("Variable '{}' does not exist.")
    return []


# Create a function in the global namespace.
# Fails if such a function is already named.
def create_new_function(scope, local):
    name = local[0]
    args = local[1]
    code = local[2]
    if name in scope.keys():
        print("Function '{}' already exists.".format(name))
    else:
        def f(scope, local):
            # confusing
            return scope['execute'](code, scope)
        scope[name] = f
        print("Created new function:", name)
    return []


def print_(scope, local):
    print(local)
    return []


def sum_(scope, local):
    return local[0] + local[1]

def difference(scope, local):
    return local[0] - local[1]

def product(scope, local):
    return local[0] * local[1]

def quotient(scope, local):
    return local[0] / local[1]
