# https://open.kattis.com/problems/anotherbrick

from sys import stdin

def main():
    # h = height, w = width, n = amount of bricks
    h, w, n = [int(x) for x in next(stdin).strip().split()]

    # List of bricks represented by their width
    bricks = [int(x) for x in next(stdin).strip().split()]

    can_complete = True
    i = 0
    width = 0
    while i < n:
        if width < w:
            width += bricks[i]
        if width == w:
            width = 0
        if width > w: # Unable to complete
            can_complete = False
            break
        i += 1

    # Output:
    if can_complete:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()

