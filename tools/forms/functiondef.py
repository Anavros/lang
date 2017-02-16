
def standard(f):
    base = "def {name}{params}"
    if f.ret:
        base += " returns {ret}"
    return base.format(**f.__dict__)


def mathematical(f):
    base = "def {name}{params}"
    if f.ret:
        base += " : {ret}"
    return base.format(**f.__dict__)
