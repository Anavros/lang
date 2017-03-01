
# file = open("myfile.txt", 'r') err stdin
# file = default(open("myfile.txt", 'r'), sys.stdin)


class Success:
    def __init__(self, value):
        self.result = value


class Failure:
    def __init__(self):
        pass


def force(result):
    """
    Return the result if successful, else raise an exception.
    """
    if   type(result) is Success:
        return result.value
    elif type(result) is Failure:
        raise Exception()
    else:
        raise ValueError()


def default(result, fallback):
    """
    Return the value of the result if successful, else return the fallback.
    """
    if   type(result) is Success:
        return result.value
    elif type(result) is Failure:
        return fallback


def read_file(path):
    try:
        return Success(open(path, 'r'))
    except IOError:
        return Failure()
