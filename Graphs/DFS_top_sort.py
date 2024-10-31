
# G is a directed, acyclic graph, returns list of vertices topologically sorted
def DFS_top_sort(G):
    stack = []
    visited = set()
    for u in G.V:
        if u not in visited:
            DFSVisit(G, u, visited, stack)
    return stack[::-1]

def DFSVisit(G, u, visited, stack):
    visited.add(u)
    for v in G.E[u]:
        if v not in visited:
            DFSVisit(G, v, visited, stack)
    stack.append(u)