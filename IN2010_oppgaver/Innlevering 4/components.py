from graph import build_graph
from collections import deque

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    components = find_components(G)
    print_components(components)


def find_components(G, visited = set()):
    components = dict()
    for k in G.V:
        v = G.V[k]
        if v not in visited:
            counter = component_size(G, v, visited)
            if counter in components:
                components[counter] += 1
            else:
                components[counter] = 1
    return components


def component_size(G, s, visited, counter = 0):
    visited.add(s)
    queue = deque()
    queue.appendleft(s)
    while len(queue) != 0:
        v = queue.pop()
        counter += 1
        for u in G.E[v]:
            if u not in visited:
                visited.add(u)
                queue.appendleft(u)
    return counter


def print_components(components):
    keys = []
    for c in components:
        keys.append(c)
    keys.sort(reverse=True)
    for k in keys:
        print(f"There are {components[k]} components of size {k}")


if __name__ == "__main__":
    main()