from graph import Graph
from collections import deque

def main():
    G = test_graph()
    DFSFull(G)

def DFSVisit(G, u, visited):
    print(u)
    visited.append(u)
    for v in G.getEdge(u):
        if v not in visited:
            DFSVisit(G, v, visited)

def DFSFull(G):
    visited = []
    for v in G.V:
        if v not in visited:
            DFSVisit(G, v, visited)
    

def test_graph():
    G = Graph()
    G.addVertex("a")
    G.addVertex("b")
    G.addVertex(3)
    G.addVertex(4)
    G.addVertex(5)
    G.addVertex(6)
    G.addVertex(7)
    G.addEdge("a", "b")
    G.addEdge("b", 3)
    G.addEdge("a", 5)
    G.addEdge(5, 4)
    G.addEdge(3, 6)
    return G


if __name__ == "__main__":
    main()