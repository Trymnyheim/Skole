# https://open.kattis.com/problems/2048

from sys import stdin

def main():
    input = []
    for _ in range(4):
        line = [int(x) for x in next(stdin).split(" ")]
        input.append(line)
    move = int(next(stdin))

    if move == 0:
        left(input)
    if move == 1:
        up(input)
    if move == 2:
        right(input)
    if move == 3:
        down(input)


def left(input):
    output = []
    for row in input:
        operate_row(row)

def up(input):
    ...

def right(input):
    ...

def down(input):
    ...


def operate_row(row):
    ...
        



if __name__ == "__main__":
    main()