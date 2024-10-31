from collections import deque

def BFSVisit(G, u, visited = []):
    visited.append(u)
    q = deque()
    q.appendleft(u)
    while len(q) != 0:
        u = q.pop()
        print(u)
        for v in G.getEdge(u):
            if v not in visited:
                visited.append(v)
                q.appendleft(v)

def BFSFull(G):
    visited = []
    for v in G.V:
        if v not in visited:
            BFSVisit(G, v, visited)