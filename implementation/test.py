
from interpreter import executor
from parser.lexer import lexer
from parser.yacker import yacker


def main():
    with open('example.malt', 'r') as f:
        source = f.read()
    lexer.input(source)
    program = yacker.parse(source, lexer)
    executor.start(program)


if __name__ == '__main__':
    main()
