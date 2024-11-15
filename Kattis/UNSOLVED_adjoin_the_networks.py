# https://open.kattis.com/problems/adjoin

# Not solved properly yet

from sys import stdin
from collections import deque
import math

def main():
    nodes, cables = [int(x) for x in next(stdin).rstrip().split(" ")]
    # Creates graph and adds the nodes
    G = dict()
    for i in range(nodes):
        G[i] = set()
    # Adds edges to graph
    counter = 0
    while counter < cables:
        node1, node2 = [int(x) for x in next(stdin).rstrip().split(" ")]
        G[node1].add(node2)
        G[node2].add(node1)
        counter += 1
    # Finds the two components of the graph
    components = find_components(G)

    max_dist = math.inf
    # Iterates over every possible combination of nodes in the two components
    for node1 in components[0]:
        for node2 in components[1]:
            G[node1].add(node2) # Adds temporary connections
            G[node2].add(node1)
            dist = find_max_dist(G)
            if dist < max_dist:
                max_dist = dist
            G[node1].remove(node2) # Removes connection again
            G[node2].remove(node1)
    print(max_dist)

# Return list of component sets in graph
def find_components(G):
    visited = set()
    components = []
    for v in G:
        if v not in visited:
            component = DFS_visit(G, v, visited, set())
            components.append(component)
    return components


# Traverses the component
def DFS_visit(G, s, visited, component):
    if s not in visited:
        visited.add(s)
        component.add(s)
        for u in G[s]:
            DFS_visit(G, u, visited, component)
    return component


# Finds max distance between two nodes in the graph
def find_max_dist(G):
    max_dist = 0
    for v in G:
        max_dist = max(max_dist, bfs_farthest(G, v))
    return max_dist


# Returns the farthest reachable distance from a node
def bfs_farthest(G, s):
        dist = [-1] * len(G)
        dist[s] = 0
        queue = deque([s])
        farthest_dist = 0
        while queue:
            v = queue.popleft()
            for u in G[v]:
                if dist[u] == -1:  # If not visited
                    dist[u] = dist[v] + 1
                    queue.append(u)
                    farthest_dist = max(farthest_dist, dist[u])
        return farthest_dist

if __name__ == "__main__":
    main()