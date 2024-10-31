import sys

# G is a directed, acyclic graph with dictionaries for
# ingoing og outgoing edges

def topsort(G):
    stack = []
    result = []
    for v in G:
        if len(G.ingoing[v]) == 0:
            stack.append(v)
    while 0 < len(stack):
        v = stack.pop()
        result.append(v)
        for u in G.outgoing[v]:
            G.ingoing[u].discard(v)
            if len(G.ingoing[u]) == 0:
                stack.append(u)
    if len(result) < len(G.V):
        sys.exit("Graph contains cycle, not sortable.") 
    return result