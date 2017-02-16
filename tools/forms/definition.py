
def standard(a):
    return "def {name} = {value}".format(**a.__dict__)


def simple(a):
    return "{name} = {value}".format(**a.__dict__)
