
def standard(f):
    base = "def {name}({params})"
    if f.ret:
        base += " returns {ret}"
    base += " {{ }}"
    return base.format(**f.__dict__)
