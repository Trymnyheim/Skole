from directed_graph import DirectedGraph
from DFS_top_sort import DFS_top_sort
from strongly_connected_components import find_strongly_connected

def main():
    test_input = [
        {
            "element": "A",
            "edges": ["B"]
        },
        {
            "element": "B",
            "edges": ["E", "F", "C"]
        },
        {
            "element": "C",
            "edges": ["D", "G"]
        },
        {
            "element": "D",
            "edges": ["C", "H"]
        },
        {
            "element": "E",
            "edges": ["A", "F"]
        },
        {
            "element": "F",
            "edges": ["G"]
        },
        {
            "element": "G",
            "edges": ["F"]
        },
        {
            "element": "H",
            "edges": ["D", "G"]
        }
    ]

    G = build_graph(test_input)
    components = find_strongly_connected(G)


def build_graph(input):
    G = DirectedGraph()
    for n in input:
        element = n["element"]
        G.addVertex(element)
        for u in n["edges"]:
            G.addEdge(element, u)
    return G


if __name__ == "__main__":
    main()