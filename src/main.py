import sys
from enums import Direction, State, Symbol
import parser
import encoder

class Handler():
    def __init__(self, inputs, rules):
        self.padding = Symbol.by_rep("_")
        self.rules = rules
        self.tape = inputs
        self.index = 0
        self.state = State(0)

    def update(self):
        if self.index == 0:
            self.tape = [self.padding] + self.tape
            self.index = 1

        if self.index == len(self.tape) - 1:
            self.tape += [self.padding]

    def next(self):
        self.update()
        state, symbol, direction = self.rules[self.state][self.tape[self.index]]
        self.state = state
        self.tape[self.index] = symbol
        offset = self.move(direction)
        self.index += offset

        return symbol, offset

    def move(self, direction):
        if direction.name == "NONE":
            return 0
        return -1 if direction.name == "RIGHT" else 1

def main():
    print("rules:")
    rules = parser.parse(sys.argv[1])
    parser.display(rules)

    print("inputs:")
    inputs = encoder.encode(sys.argv[2])
    encoder.display(inputs)

    h = Handler(inputs, rules)
    symbol, direction = h.next()


if __name__ == '__main__':
    main()
