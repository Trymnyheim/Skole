from sys import stdin
from collections import defaultdict

def main():
    N = int(next(stdin))
    G = Graph()
    while N > 0:
        input = [int(x) for x in next(stdin).strip().split(" ")]
        vertex = input[0]
        edges = input[1:]
        G.addVertex(vertex, edges)
        N -= 1
    G.print_graph()


class Graph:
    def __init__(self):
        self.V = set()
        self.E = defaultdict(set)

    def addVertex(self, val, edges):
        self.V.add(val)
        for u in edges:
            self.V.add(u)
            self.E[val].add(u)
            self.E[u].add(val)
        
    def print_graph(self):
        for v in self.V:
            print(v)
            print(self.E[v])
            print()

if __name__ == "__main__":
    main()
