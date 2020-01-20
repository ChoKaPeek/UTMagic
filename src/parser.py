from enums import Direction, State, Symbol

def parse(f):
    dic = {}
    content = read(f)
    transitions = content.split("\n\n")

    print(transitions[0])
    transitions = transitions[1:]

    for t in transitions:
        try:
            src, dst = t.split("\n")
        except:
            if len(t.split("\n")) == 1:
                break
            src, dst, _ = t.split("\n")

        state, symbol = src.split(",")
        state_key = State.by_rep(state)
        symbol_key = Symbol.by_rep(symbol)

        if state_key not in dic:
            dic[state_key] = {}
        dic[state_key].update({symbol_key: make_tuple(dst)})

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

def display(dic):
    symbol_len = max(get_max_length(Symbol), len("Symbol"))
    new_state_len = max(get_max_length(State), len("New State"))
    new_symbol_len = max(get_max_length(Symbol), len("New Symbol"))
    direction_len = max(get_max_length(Direction), len("Direction"))
    total = symbol_len + new_state_len + new_symbol_len + direction_len + 11

    for state, value in dic.items():
        print(f"State: {state.name}")
        print("+" + "-" * total + "+")
        pprint("Symbol", symbol_len)
        pprint("New State", new_state_len)
        pprint("New Symbol", new_symbol_len)
        pprint("Direction", direction_len, last=True)
        for symbol, tupl in value.items():
            pprint(symbol.name, symbol_len)
            pprint(tupl[0].name, new_state_len)
            pprint(tupl[1].name, new_symbol_len)
            pprint(tupl[2].name, direction_len, last=True)

        print("+" + "-" * total + "+")
        print("")

def get_max_length(enum):
    return max([len(e.name) for e in enum])

def pprint(txt, nb, last=False):
    if last:
        print("| " + " " * (nb - len(txt)) + txt + " |")
    else:
        print("| " + " " * (nb - len(txt)) + txt + " ", end='')
