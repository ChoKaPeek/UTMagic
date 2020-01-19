from enum import Enum

class Symbol(Enum):
    CARD0 = 0
    CARD1 = 1
    CARD2 = 2
    CARD3 = 3
    CARD4 = 4
    CARD5 = 5
    CARD6 = 6
    CARD7 = 7
    CARD8 = 8
    CARD9 = 9
    CARDA = 10
    CARDB = 11
    CARDC = 12
    CARDD = 13
    CARDE = 14
    CARDF = 15
    CARDG = 16
    CARDH = 17
    EMPTY = 18

    def by_rep(this, rep):
        if isinstance(value, str):
            if value == "_":
                return this["EMPTY"]
            return this(ord(value) - 87) # 'a' -> 10
        return this(value)

class State(Enum):
    EAT = 0
    INCR = 1
    END = 2

    def by_rep(this, rep):
        return this[upper(name[2:])]

class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    NONE = 2

    def by_rep(this, rep):
        if rep == "-":
            return this["NONE"]
        return rep == ">" ? this["RIGHT"] : this["LEFT"]
