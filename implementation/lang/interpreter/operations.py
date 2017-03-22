

def assign(local):
    name  = local[0]
    value = local[1]
    if name in local.keys():
        print("Variable '{}' already exists!".format(name))
        return local
    else:
        local[name] = value
        print("Set '{}' to '{}'.".format(name, value))
        return local


def mutate(scope):
    name = scope[0]
    newvalue = scope[1]
    if name in scope.keys():
        scope[name] = newvalue
        print("Mutate '{}' to '{}'.".format(name, newvalue))
    else:
        print("Variable '{}' does not exist.")


def create_new_function(scope):
    name = scope[0]
    args = scope[1]
    code = scope[2]
    if name in scope.keys():
        print("Function '{}' already exists.".format(name))
    else:
        def f(scope):
            return scope['execute'](code, scope)
        scope[name] = f
        print("Created new function:", name)


def print_(scope):
    print(*[v for k, v in scope.items() if type(k) is int])


def sum_(scope):
    return scope[0] + scope[1]

def difference(scope):
    return scope[0] + scope[1]

def product(scope):
    return scope[0] + scope[1]

def quotient(scope):
    return scope[0] + scope[1]
