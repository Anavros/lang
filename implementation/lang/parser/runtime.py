
from lang.objects import *


values = {}

stdlib = {
    'sum': sum,
}


def evaluate_variable(name):
    if name in values.keys():
        return values[name]
    else:
        raise KeyError("Variable '{}' is not defined.".format(name))


def add_variable(name, value):
    #print("DEFINE {} = {}".format(name, value))
    values[name] = value;


def evaluate_function(name, args):
    #print("Evaluating...", name, args)
    if name in stdlib.keys():
        return stdlib[name](args)
    else:
        raise KeyError("Unknown function '{}'.".format(name))
