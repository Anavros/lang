
from sys import argv
import malt


def main():
    guide = style(argv[1])
    template(guide)


def style(path):
    guide = {}
    options = [
        "assignment form",
        "function form",
    ]
    for line in malt.load(path, options):
        guide[line._head] = line.form
    return guide


def template(guide):
    options = [
        "assignment type name value",
        "function name arg1 arg2 type return"
    ]
    for line in malt.load("template.malt", options):
        print(guide[line._head].format(**line))


if __name__ == '__main__':
    main()
