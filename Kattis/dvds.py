# https://open.kattis.com/problems/dvds

from sys import stdin

def main():
    t = int(next(stdin))
    for _ in range(t):
        n = int(next(stdin))
        stack = [int(x) for x in next(stdin).split()]
        print(adjustments(n, stack))

def adjustments(n, stack):
    steps = 0
    next = 1
    for n in stack:
        if n != next:
            steps += 1
        else:
            next += 1
    return steps


if __name__ == "__main__":
    main()