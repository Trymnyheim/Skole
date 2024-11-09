# https://open.kattis.com/problems/sortofsorting

from sys import stdin

def main():
    cases = [] # Stores all cases
    n = int(next(stdin).strip()) # Number of names in case
    while n != 0:
        names = []
        for _ in range(n):
            names.append(next(stdin).strip()) # Reads and adds names to namelist
        cases.append(names)
        n = int(next(stdin).strip()) # n names in next case

    # Sorts every name list in cases:
    for names in cases:
        bubble_sort(names, 2) # Sorts first on second letter
        bubble_sort(names, 1) # Then on first

    # Output:
    for names in cases:
        for name in names:
            print(name)
        if names != cases[len(cases)-1]: # No newline if last case
            print()


# Sorts names on string index nr - 1
def bubble_sort(names, nr):
    for i in range(len(names) - 1):
        for j in range(len(names) - 1):
            if names[j][nr-1] > names[j+1][nr-1]:
                names[j], names[j+1] = names[j+1], names[j]


if __name__ == "__main__":
    main()