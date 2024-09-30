from collections import defaultdict
from graph import build_graph
from heapq import heappush, heappop
import math

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    testdata = [
        ["nm2255973", "nm0000460"],
        ["nm0424060", "nm8076281"],
        ["nm4689420", "nm0000365"],
        ["nm0000288", "nm2143282"],
        ["nm0637259", "nm0931324"]
    ]
    for inp in testdata:
        weight, path = dijkstra(G, inp[0], inp[1])
        print_path(path, weight)


# Finds path with highest rated movies between actors
def dijkstra(G, s, target):
    s = G.V[s]
    target = G.V[target]
    dist = defaultdict(lambda: math.inf)
    dist[s] = 0
    queue = [(0, s)]
    parent = {} # To store the shortest path
    while queue:
        dist_u, u = heappop(queue)  
        if u == target:
            break  
        for v in G.E[u]: 
            movie = G.get_highest_rated(u, v)  # Returns highest rated movie
            c = dist_u + (10 - movie.rating)  # Calculation cost of edge
            if c < dist[v]:
                dist[v] = c
                parent[v] = u 
                heappush(queue, (c, v))  
    # Reconstructing the path
    path = []
    current = target
    while current in parent:
        mov = G.get_highest_rated(parent[current], current)
        path.append([current, mov, mov.rating])
        current = parent[current]
    path.append(s) 
    path.reverse()
    return dist[target], path


def print_path(path, weight):
    print("\n", path[0])
    for edge in path[1:]:
        actor, movie, rating = edge
        print(f"=== [ {movie} ({round(rating, 1)})] ===> {actor}")
    print(f"Total weight: {round(weight, 1)}\n")


if __name__ == "__main__":
    main()
