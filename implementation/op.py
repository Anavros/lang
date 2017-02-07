
from constants import *


def do(code, args, state):
    global codes
    try:
        codes[code](args, state)
    except KeyError:
        print("Unknown function: '{}'.".format(code))


def op_print(args, state):
    for val in args:
        if val.t == T_CONSTANT:
            print(val.value, end=' ')
        else:
            try:
                lit = state[val.value]
            except KeyError:
                print("NameError: '{}'.".format(val.value))
            else:
                print(lit, end=' ')
    print()


def op_assign(args, state):
    state[args[0].value] = args[1].value


def op_exit(args, state):
    pass


# This should be part of the state probably.
codes = {
    "print": op_print,
    "assign": op_assign,
    "exit": op_exit,
}
