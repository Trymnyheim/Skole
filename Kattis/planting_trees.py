# https://open.kattis.com/problems/plantingtrees

from sys import stdin

def main():
    N = int(next(stdin).strip())
    times = [int(x) for x in next(stdin).strip().split()]

    times.sort()
    times.reverse()

    finished = []
    for i in range(1, N + 1):
        finished.append(i + times[i-1] + 1)

    print(max(finished))

if __name__ == "__main__":
    main()
