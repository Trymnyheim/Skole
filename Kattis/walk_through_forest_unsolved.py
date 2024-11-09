# https://open.kattis.com/problems/walkforest

from sys import stdin
import math
from heapq import heappush, heappop
from collections import deque

def main():
    outputs = [] # Keeps track of output numbers
    input = next(stdin).strip()
    while input != "0":
        N, M = [int(x) for x in input.split()] # N nodes, M edges

        graph = dict() # Graph
        weight = dict() # Weight of edges

        for i in range(N):
            graph[i+1] = set()

        # Read info about edges:

        for _ in range(M):
            v, u, w = [int(x) for x in next(stdin).strip().split()] # Edge from node v to u with weight w
            graph[v].add(u)
            graph[u].add(v) # Directional???
            weight[(v, u)] = w
            weight[(u, v)] = w


        shortest_paths = dijkstra(graph, weight, 1)
        paths = bfs_count_paths(shortest_paths, 2)

        # Adds results to output:
        outputs.append(paths[1])

        # Reads next line of input
        input = next(stdin).strip()

    # Prints output
    for n in outputs:
        print(n)


# Counts paths from start node s
def bfs_count_paths(graph, s):
    visited = set()
    queue = deque()
    paths = {s: 1} # Keeps track of amount of paths to every node
    queue.append(s)
    visited.add(s)
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if u not in visited and u != 1:
                queue.append(u)
                visited.add(u)
            if u in paths:
                paths[u] += paths[v]
            else:
                paths[u] = paths[v]
    return paths

# Finds all shortest paths
def dijkstra(graph, weight, start):
    dist = {node: math.inf for node in graph}
    parents = {node: set() for node in graph}
    for node in graph:
        dist[node] = math.inf
    dist[start] = 0
    queue = [(0, start)] # Priority queue
    while queue:
        c, v = heappop(queue)
        for u in graph[v]:
            distance = c + weight[(v, u)]
            if distance < dist[u]:  # Found a shorter path to u
                parents[u] = {v}
                dist[u] = distance
                heappush(queue, (dist[u], u))
            elif distance == dist[u]:  # Found an alternate shortest path
                parents[u].add(v)
    return parents

if __name__ == "__main__":
    main()
