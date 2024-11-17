# https://open.kattis.com/problems/coloring

from sys import stdin
from collections import defaultdict

def main():
    # Get and process all input:
    N = int(next(stdin))
    data = [] # Collects all input
    vertices = set()
    for _ in range(N):
        input = [int(x) for x in next(stdin).strip().split()]
        data.append(input)
        [vertices.add(x) for x in input]
    
    # Build graph:
    graph = dict()
    for v in vertices:
        graph[v] = set()
    for line in data:
        if len(line) > 1:
            v = line[0]
            for u in line[1:]:
                graph[v].add(u)
    print(graph)

if __name__ == "__main__":
    main()
