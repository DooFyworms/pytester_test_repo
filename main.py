import os
import math



def add(a, b) -> int:
    return math.floor(a + b)


def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'


def sub(a, b) -> int:
    return math.floor(a - b)


if __name__ == "__main__":
    print(os.path.dirname(__file__))

