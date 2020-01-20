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
    CARD_ = 17

    @classmethod
    def by_rep(cls, rep):
        rep = rep.lower()
        try:
            return cls(int(rep))
        except ValueError:
            if rep == "_":
                return cls["CARD_"]
            return cls(ord(rep) - 87) # 'a' -> 10

    @classmethod
    def max_len(cls, title):
        return max([len(e.name) - len("CARD") for e in cls] + [len(title)])


class State(Enum):
    EAT = 0
    INCR = 1
    END = 2

    @classmethod
    def by_rep(cls, rep):
        return cls[rep[2:].upper()]

    @classmethod
    def max_len(cls, title):
        return max([len(e.name) for e in cls] + [len(title)])


class Direction(Enum):
    RIGHT = 0
    LEFT = 1
    NONE = 2

    @classmethod
    def by_rep(cls, rep):
        if rep == "-":
            return cls["NONE"]
        return cls["RIGHT"]  if rep == ">" else cls["LEFT"]

    @classmethod
    def max_len(cls, title):
        return max([len(e.name) for e in cls] + [len(title)])
