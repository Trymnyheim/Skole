from graph import Graph

# Returns false if separation nodes exist, else True
def is_biconnected(G):
    if len(sep_vertices(G)) == 0:
        return True
    return False


# Traversion of connected graph, returns list of seperation nodes
def sep_vertices(G):
    depth = dict() # Tracks a vertex's depth
    low = dict() # Tracks the lowest depth reachable directly or through a child
    seps = set()
    s = G.V[0] # Arbitrary start vertex
    depth[s] = 0
    low[s] = 0
    children = 0
    for u in G.E[s]:
        if u not in depth:
            sep_rec(G, s, u, 1, depth, low, seps)
            children += 1
    # if root has more than 1 child, add s to seps
    if children > 1:
        seps.add(s)
    return seps


# p for parent, u for node being visited, d for nodes depth nr
def sep_rec(G, p, u, d, depth, low, seps):
    depth[u] = d
    low[u] = d
    for v in G.E[u]:
        if v == p:
            # v is the parent of u
            continue
        if v in depth:
            low[u] = min(low[u], depth[v]) # depth[v] is childs depth
        else:
            # Continues recursive visits:
            sep_rec(G, u, v, d + 1, depth, low, seps)
            low[u] = min(low[u], low[v]) # low[v] is childs low nr
            if d <= low[v]: # No backedges from u's subtree
                seps.add(u)