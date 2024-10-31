from collections import deque
from graph import build_graph

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    test_data = [
        ["nm2255973", "nm0000460"],
        ["nm0424060", "nm8076281"],
        ["nm4689420", "nm0000365"],
        ["nm0000288", "nm2143282"],
        ["nm0637259", "nm0931324"]
    ]
    for inp in test_data:
        path = shortest_path(G, inp[0], inp[1])
        print_path(path)


def shortest_path(G, s, target):
    s = G.V[s]
    target = G.V[target]
    found = False
    visited = set()
    queue = deque()
    queue.append(s)
    parents = dict()
    while len(queue) != 0:
        v = queue.popleft()
        for u in G.E[v]:
            if u not in visited:
                parents[u] = v
                queue.append(u)
                visited.add(u)
                if u == target:
                    found = True
                    break
    if found:
        path = []
        current = target
        while current is not s:
            mov = next(iter(G.W[(parents[current], current)]))
            path.append([current, mov, mov.rating])
            current = parents[current]
        path.append(s)
        path.reverse()
        return path
    return None


def print_path(path):
    print("\n", path[0])
    for edge in path[1:]:
        actor, movie, rating = edge
        print(f"=== [ {movie} ({round(rating, 1)})] ===> {actor}")
    print()


if __name__ == "__main__":
    main()