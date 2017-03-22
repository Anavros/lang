
import lang
from sys import argv

command = argv[1]

with open('example.malt', 'r') as f:
    source = f.read()

if command == "run":
    lang.run(source)
elif command == "tokens":
    lang.dump_tokens(source)
elif command == "ast":
    lang.dump_ast(source)
