
DEBUG = True

def debug(*messages):
    if DEBUG:
        print("DEBUG:", end="")
        print(*messages)
