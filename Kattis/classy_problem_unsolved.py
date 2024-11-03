# https://open.kattis.com/problems/classy

# Unsolved

from sys import stdin
from heapq import heappush, heappop

def main():
    # Gets input and arranges it into cases:
    T = int(next(stdin)) # Number of cases
    cases = []
    for _ in range(T):
        n = int(next(stdin)) # Number of objects in case
        names = dict()
        for _ in range(n):
            object, classes = next(stdin).strip().split(": ")
            classes, _ = classes.split() # Get rid of the " class"
            names[object] = [c for c in classes.split("-")]
            while len(names[object]) != 10:
                names[object].append("middle")
        cases.append(names)

    # Sorts and writes output:
    for names in cases:
        names = radix_sort(names)
        for name in names:
            print(name)
        print("=" * 30)


def radix_sort(names):
    sorted_names = list(names.keys())  # Start with a list of names
    d = 10  # Number of class levels to consider
    while d > 0:
        sorted_names = bucket_sort(names, sorted_names, d)
        d -= 1
    return sorted_names


def bucket_sort(names, sorted_names, i):
    # Initialize buckets:
    B = {
        "upper": [],
        "middle": [],
        "lower": []
    }
    # Fill buckets
    for name in sorted_names:
        class_rank = names[name][i - 1]
        B[class_rank].append(name)
    # Empty buckets:
    return B["upper"] + B["middle"] + B["lower"]

if __name__ == "__main__":
    main()
