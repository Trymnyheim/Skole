from heapq import heappush, heappop
from sys import stdin

def main():
    input = stdin.read().splitlines()
    heap = []
    for n in input:
        heappush(heap, int(n.rstrip()))
    balance(heap)


def balance(heap):
    if len(heap) > 0:
        mid = len(heap) // 2
        lowHeap = []
        highHeap = []
        while len(heap) > mid + 1:
            heappush(lowHeap, heappop(heap))
        print(heappop(heap))
        while len(heap) > 0:
            heappush(highHeap, heappop(heap))
        balance(highHeap)
        balance(lowHeap)


if __name__ == "__main__":
    main()