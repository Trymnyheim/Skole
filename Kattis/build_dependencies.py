# https://open.kattis.com/problems/builddeps

from sys import stdin, setrecursionlimit

setrecursionlimit(100000)

def main():
    input_n = int(next(stdin))
    G = dict() # Graph
    dependencies = dict()
    while input_n > 0:
        line = next(stdin).strip()
        if ':' in line:
            node, deps = line.split(":")
            deps = deps.strip().split() if deps else []
        else:
            node, deps = line, []
        dependencies[node] = deps
        G[node] = set() # Adding nodes to graph
        input_n -= 1

    # File that will be changed
    changed_file = next(stdin).strip()
    
    # Adding deps as directed edges
    for node in dependencies:
        for dep in dependencies[node]:
            if dep:
                G[dep].add(node)

    sorted = find_dependencies(G, changed_file)

    # Output results:
    for node in sorted:
        print(node)


# TopSort using DFS
def find_dependencies(G, s):
    visited = set()
    sorted = []
    dfs(G, s, visited, sorted)   
    return list(reversed(sorted))


def dfs(G, v, visited, sorted):
    if v not in visited:
        visited.add(v)
        for u in G[v]:
            dfs(G, u, visited, sorted)
        sorted.append(v)

if __name__ == "__main__":
    main()
    