import sys
from enums import Symbol
import parser

def main():
    dic = parser.parse(sys.argv[1])
    parser.display(dic)

    print(f"input: {sys.argv[2]}")
    inputs = []
    for c in sys.argv[2]:
        inputs.append(Symbol.by_rep(c))

    for i in inputs:
        print(f"{i.value}: {i.name}")

if __name__ == '__main__':
    main()
