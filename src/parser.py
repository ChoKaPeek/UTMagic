from enums import Direction, State, Symbol

def parse(f):
    dic = {0: {}, 1: {}}
    content = read(f)
    transitions = content.split("\n\n")

    print(transitions[0])
    transitions = transitions[1:]

    for t in transitions:
        src, dst = t.split("\n")
        state, symbol = src.split(",")

        dic[State.by_rep(state)][Symbol.by_rep(symbol)] = make_tuple(dst)

    return dic

def make_tuple(dst):
    state, symbol, direc = dst.split(",")
    return (State.by_rep(state), Symbol.by_rep(symbol), Direction.by_rep(direc))

def read(f):
    content = ""
    try:
        with open(f, "r") as fd:
            content = fd.read()
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, IsADirectoryError) as err:
        raise err
    return content
