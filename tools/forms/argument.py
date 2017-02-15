
def standard(a):
    if a.key:
        base = "{key} = {value}"
    else:
        base = "{value}"
    if a.option:
        base += '?'
    if a.mut:
        base += '!'
    return base.format(**a.__dict__)
