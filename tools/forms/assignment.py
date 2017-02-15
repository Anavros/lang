
def standard(a):
    return "{name} = {value}".format(**a.__dict__)


def no_equals(a):
    return "def {name} {value}".format(**a.__dict__)
