
from lang.objects import *


def evaluate_function(f):
    print("Evaluating...", f.name, f.args)
    if f.name == 'sum':
        a, b = [x.val for x in f.args.values]
        return Value(0, sum([a, b]))
    else:
        return f
