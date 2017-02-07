
import lexer
import yacker
import executor

with open('example.malt', 'r') as f:
    source = f.read()

lexer.lexer.input(source)
result = yacker.run(source, lexer.lexer)
executor.run(result)
