from random import sample


def make_bingo():
    data = sample(range(1, 76), 25)
    result = [data[i:i + 5] for i in range(0, 25, 5)]
    result[2][2] = 0
    return tuple(map(tuple, result))