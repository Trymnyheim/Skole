from graph import build_graph

def main():
    G = build_graph("input/movies.tsv", "input/actors.tsv")
    components = find_components(G)
    print_components(components)
    

def component_size(G, v, visited = {}, counter = 0):
    visited.add(v)
    counter += 1
    for u in G.E[v]:
        if u not in visited:
            component_size(G, u, visited, counter)
    return counter


def find_components(G, visited = {}):
    components = dict()
    for k in G.V:
        v = G.V[k]
        if v in visited:
            counter = component_size(G, v, visited)
            if counter in components:
                components[counter] += 1
            else:
                components[counter] = 1
    return components


def print_components(components):
    for c in components.sort():
        print(f"There are {components[c]} components of size {c}")