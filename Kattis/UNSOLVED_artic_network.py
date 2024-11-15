# https://open.kattis.com/problems/arcticnetwork

from sys import stdin
import math

n_cases = int(next(stdin).strip())

for _ in range(n_cases):
    # S amounts of satelite channels, P amounts of outposts
    S, P = [int(x) for x in next(stdin).strip().split()]

    outposts = [] # Stores x and y coordinates of outposts as tuples
    for _ in range(P):
        x, y = [int(x) for x in next(stdin).strip().split()]
        outposts.append((x, y))

def get_hypotenuse(side1, side2):
    return math.sqrt(side1**2 + side2**2)