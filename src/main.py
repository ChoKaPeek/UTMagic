import sys
from enums import Direction, State, Symbol
import parser
import encoder

class Handler():
    def __init__(self, argv):
        self.rules = parser.parse(argv[1])
        self.tape = encoder.encode(argv[2])
        self.init_tape = self.tape
        self.padding = Symbol.by_rep("_")
        self.index = 0
        self.state = State(0)

    def get_init(self):
        return ["_"] * 3 + [e.name[4] for e in self.init_tape] + ["_"] * 1

    def update(self):
        if self.index == 0:
            self.tape = [self.padding] + self.tape
            self.index = 1

        if self.index == len(self.tape) - 1:
            self.tape += [self.padding]

    def next(self):
        self.update()
        state, symbol, direction = self.rules[self.state][self.tape[self.index]]
        changed = state.value != self.state.value
        self.state = state
        self.tape[self.index] = symbol
        offset = self.move(direction)
        self.index += offset

        return changed, symbol.name[4], offset # bool, char, int

    def move(self, direction):
        if direction.name == "NONE":
            return 0
        return 1 if direction.name == "RIGHT" else -1

    def display(self):
        print("rules:")
        parser.display(self.rules)
        print("tape:")
        encoder.display(self.tape)

def main():
    h = Handler(sys.argv)
    h.display()


if __name__ == '__main__':
    main()
