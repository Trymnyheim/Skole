from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.V = set()
        self.E = defaultdict(set)

    def addVertex(self, x):
        self.V.add(x)

    def addEdge(self, v1, v2):
        self.E[v1].add(v2)

    def getEdges(self, v):
        return self.E[v]