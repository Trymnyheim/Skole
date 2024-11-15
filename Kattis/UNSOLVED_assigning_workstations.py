# https://open.kattis.com/problems/workstations

from sys import stdin
from heapq import heappush, heappop

def main():
    # n researches, computer locks after m minutes
    n, m = [int(x) for x in next(stdin).strip().split()]

    # read inputlines
    researchers = []
    for _ in range(n):
        start, end = [int(x) for x in next(stdin).strip().split()]
        researchers.append([start, start + end])

    # Calculate results
    researchers = sorted(researchers)
    counter = 0
    actives = []
    for s, e in researchers:
        if actives and actives[0] <= s <= actives[0] + m:
            counter += 1
            heappop(actives)
        heappush(actives, e)

    # Output:
    print(counter)

if __name__ == "__main__":
    main()

