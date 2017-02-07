

class State:
    def __init__(self):
        self.quoted = False
        self.keybuf = []
        self.strbuf = []
        self.groupstack = []
        self.tokens = []


def parse(f):
    state = State()
    while True:
        c = f.read(1)
        if not c:
            break
        elif c in WHITESPACE:
            space(c, state)
        elif c == DOUBLE_QUOTE:
            quote(c, state)
        elif c in GROUPS:
            group(c, state)
        elif c == STATEMENT:
            conclude(c, state)
        else:
            other(c, state)
    return state.tokens


def space(c, state):
    if state.quoted:
        # TODO: ignore newlines in quoted strings
        state.strbuf.append(c)


def other(c, state):
    if state.quoted:
        state.strbuf.append(c)
    else:
        state.keybuf.append(c)


def quote(c, state):
    if state.quoted:
        state.quoted = False
        state.tokens.append(''.join(state.strbuf))
        state.strbuf = []
    else:
        state.quoted = True


def group(c, state):
    pass


def conclude(c, state):
    if state.keybuf:
        state.tokens.append(''.join(state.keybuf))
        state.keybuf = []
