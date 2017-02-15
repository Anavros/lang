

def _app(base, p):
    if p.option:
        base += '?'
    if p.mut:
        base += '!'
    return base.format(**p.__dict__)


def standard(p):
    base = "{type} {name}"
    return _app(base, p)


def mathematical(p):
    base = "{name}:{type}"
    return _app(base, p)
