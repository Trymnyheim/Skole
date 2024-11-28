# https://open.kattis.com/problems/skolavslutningen/

from sys import stdin

def main():
    N, M, K = [int(x) for x in next(stdin).strip().split()]

    A = [[] for i in range(N)]

    cols = [set() for i in range(M)]
    for i in range(N):
        line = next(stdin).strip()
        for j, let in enumerate(line):
            cols[j].add(let)

    visited = set()
    counter = 0
    for i in range(len(cols)):
        if visited.intersection(cols[i]):
            for let in cols[i]:
                visited.add(let)
        else:
            counter += 1
            for let in cols[i]:
                visited.add(let)
    print(counter)

if __name__ == "__main__":
    main()
