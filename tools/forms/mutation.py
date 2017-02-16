
def standard(a):
    return "mut {name} = {value}".format(**a.__dict__)


def dnb(a):
    return "{name} := {value}".format(**a.__dict__)
