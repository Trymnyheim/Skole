# https://open.kattis.com/problems/pickupsticks

# Fails third test for some strange reason

from sys import stdin
from collections import deque

def main():
    # n amount of sticks, m amount stick on top of stick
    n, m = [int(x) for x in next(stdin).strip().split()] 

    # Creating graph
    G = {i: set() for i in range(1, n + 1)}
    ingrade = {i: 0 for i in range(1, n + 1)}

    # stick a on top of b
    for _ in range(m):
        a, b = [int(x) for x in input().strip().split()]
        G[a].add(b)         # Add a on top of b
        ingrade[b] += 1     # Increment in-degree

    results = TopSort(G, ingrade) # Orders the sticks

    # Output
    if results:
        print('\n'.join(map(str, results)))
    else:
        print("IMPOSSIBLE")

# Topologically sorts nodes in graph
def TopSort(G, ingrade):
    queue = deque()
    results = []
    for i in ingrade:
        if ingrade[i] == 0:
            queue.append(i)
    while queue:
        v = queue.popleft() # Pop first node in queue
        results.append(v)
        for u in G[v]:
            ingrade[u]-= 1 # lower u's ingrade for edge from v
            if ingrade[u] == 0:
                queue.append(u)
    if len(results) != len(G): # Cycle detected
        return None      
    return results

if __name__ == "__main__":
    main()
