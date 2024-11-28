# https://open.kattis.com/problems/licensetolaunch

from sys import stdin
import math

def main():
    N = int(next(stdin).strip())
    junk = [int(x) for x in next(stdin).strip().split()]

    min = math.inf
    day = None
    for i in range(N):
        if junk[i] < min:
            min = junk[i]
            day = i
    print(day)

if __name__ == "__main__":
    main()

