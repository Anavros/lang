
def mutate(a):
    return "mut {name} = {value}".format(**a.__dict__)
