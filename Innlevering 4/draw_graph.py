import graphviz

def drawgraph(G):
    dot = graphviz.Graph()
    seen_edges = set()
    for u in G.V:
        dot.node(u.name)
        for v in G.E[u]:
            if (v, u) in seen_edges:
                continue
            seen_edges.add((u, v))
            dot.edge(u.name, v.name, label=str(G.W[(u, v)]))
    dot.render('graph', format='svg')