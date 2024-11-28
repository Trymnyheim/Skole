# https://open.kattis.com/problems/cats

from sys import stdin
from heapq import heappush, heappop

def main():
    T = int(next(stdin).strip()) # Amount of cases
    results = []
    for _ in range(T):
        # M amount of milk and C amount of cats
        M, C = [int(x) for x in next(stdin).strip().split()]
        graph = dict()
        weight = dict()
        for i in range(C):
            graph[i] = set()
        for _ in range((C * (C - 1))//2):
            u, v, w = [int(x) for x in next(stdin).strip().split()]
            graph[u].add(v)
            graph[v].add(u)
            weight[(u, v)] = w
            weight[(v, u)] = w

        _, costs = prim_minimal(graph, weight, 0)
        total = 0
        for cost in costs.values():
            total += cost
        if total <= M:
            results.append("yes")
        else:
            results.append("no")
    
    for res in results:
        print(res)


def prim_minimal(G, weight, s):
    parents = dict()
    cost = dict()
    queue = [(0, (None, s))]
    while queue:
        _, edge = heappop(queue)
        (p, u) = edge
        if u not in parents:
            parents[u] = p
            if p is not None:
                cost[u] = weight[(p, u)]
            for v in G[u]:
                heappush(queue, (weight[(u, v)],(u, v)))
    return parents, cost

if __name__ == "__main__":
    main()