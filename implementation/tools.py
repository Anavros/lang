

def chars(f):
    """
    Iterate over each character in f.
    """
    while True:
        c = f.read(1)
        if not c:
            break
        else:
            yield c


class Processor:
    def __init__(self):
        self.buf = []
        self.tokens = []

    def buffer(self, c):
        self.buf.append(c)

    def add(self, token):
        self.tokens.append(token)

    def chomp(self):
        if self.buf:
            self.tokens.append(''.join(self.buf))
            self.buf = []
