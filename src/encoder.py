from enums import Direction, State, Symbol

def encode_number(s):
    inputs = []
    for c in s:
        for rep in c:
            inputs.append(Symbol.by_rep(rep))

    return inputs

def encode(s):
    inputs = []
    for c in s:
        for rep in str(ord(c)):
            inputs.append(Symbol.by_rep(rep))
        inputs.append(Symbol.by_rep("d"))

    return inputs

def display(inputs):
    print([i.name[4] for i in inputs], sep=",")
