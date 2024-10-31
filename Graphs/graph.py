class Graph:
    def __init__(self):
        self.V = []
        self.E = {}

    def addVertex(self, x):
        self.V.append(x)
        self.E[x] = []

    def addEdge(self, v1, v2):
        self.E[v1].append(v2)
        self.E[v2].append(v1)

    def getEdge(self, v):
        return self.E[v]

    def __str__(self):
        return f"{self.V}\n{self.E}"





    
