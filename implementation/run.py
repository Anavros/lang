
if __name__ == '__main__':
    import lang
    with open('example.malt', 'r') as f:
        lang.run(lang.ast(f.read()))
