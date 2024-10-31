from DFS_top_sort import DFS_top_sort
from directed_graph import DirectedGraph

# Not working :(
def find_strongly_connected(G):
    stack = DFS_top_sort(G)
    reverse_G = reverse_graph(G)
    visited = set()
    components = []
    while len(stack) != 0:
        u = stack.pop()
        if u not in visited:
            component = []
            DFS_visit_connected(reverse_G, u, visited, component)
            print(component)
    return components


def DFS_visit_connected(G, u, visited, component):
    visited.add(u)
    component.append(u)
    for v in G.E[u]:
        if v not in visited:
            DFS_visit_connected(G, v, visited, component)


def reverse_graph(G):
    reverse = DirectedGraph()
    for v in G.V:
        reverse.addVertex(v)
    for v in G.V:
        for u in G.E[v]:
            reverse.addEdge(u, v)
    return reverse




