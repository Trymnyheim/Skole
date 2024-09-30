from collections import deque
from graph import build_graph

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    for actor in G.V:
        if actor.name == "Carrie Coon":
            node1 = actor
        if actor.name == "Julie Delpy":
            node2 = actor
    path = shortest_path(G, node1, node2)
    print()
    print(path[0], "--->")
    for e in path[1:]:
        print(f"{e[1]} --->  {e[0]}")
    print()


def shortest_path(G, s, target):
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
            mov = G.W[(parents[current], current)]
            path.append([current, mov])
            current = parents[current]
        path.append(s)
        path.reverse()
        return path
    return None


if __name__ == "__main__":
    main()