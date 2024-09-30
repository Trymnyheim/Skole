from collections import defaultdict
from graph import build_graph
from heapq import heappush, heappop
import math

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    print(len(G.V))
    print(G.getLenE())
    for actor in G.V:
        if actor.name == "Carrie Coon":
            node1 = actor
        if actor.name == "Julie Delpy":
            node2 = actor
    for n in dijkstra(G, node1, node2):
        print(n)


def dijkstra(G, s, target):
    dist = defaultdict(lambda: math.inf)
    dist[s] = 0
    queue = [(0, s)]  # Keep Actor object in the queue for easy access
    parent = {}  # To store the shortest path

    while queue:
        dist_u, u = heappop(queue)  # u is the Actor object
        
        # If we reach the target actor, we can stop early
        if u == target:
            break
        
        # Loop through all adjacent actors
        for v in G.E[u]:  # v is the adjacent Actor object
            movie = G.get_highest_rated(u, v)  # Get the highest-rated movie between u and v
            if movie:  # Check if a movie exists between them
                c = dist_u + (10 - movie.rating)  # Cost calculation
                
                # If the new path is shorter, update the distance and push to the queue
                if c < dist[v]:
                    dist[v] = c
                    parent[v] = u  # Set the predecessor
                    heappush(queue, (c, v))  # Push with distance and Actor object

    # Reconstruct the shortest path
    path = []
    current = target
    while current in parent:
        mov = G.get_highest_rated(parent[current], current)
        path.append([current, mov, mov.rating])
        current = parent[current]
    path.append(s)  # Include the source actor
    path.reverse()  # Reverse the path to get it from source to target

    return dist[target], path  # Return the distance to target and the path


if __name__ == "__main__":
    main()
