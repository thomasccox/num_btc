import math


def num_BTC(b):
    blocks = math.floor(b / 210000)
    c = float(0)
    for i in range(blocks):
        #c = c + 50 * (2 ** (-i)) * 210000
        c = c + (50*pow(2,-i)*210000)
    c = c + (50 * pow(2, -blocks) * (b % 210000))
    return c
