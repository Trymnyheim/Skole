# https://open.kattis.com/problems/horror

from sys import stdin
import math
from collections import deque

# N = n movies, H = n movies on horror list, L = n similarities in DB
N, H, L = [int(x) for x in next(stdin).split()]

horror_ids = [int(x) for x in next(stdin).split()]

# Building graph
G = dict()
for i in range(N):
    G[i] = set()
while L != 0:
    a, b = [int(x) for x in next(stdin).split()]
    G[a].add(b)
    G[b].add(a)
    L -= 1

# Horror index initialized with infinite as value
horror_index = {v: math.inf for v in range(N)}

# BFS for updating horror index
queue = deque(horror_ids) # Enqueue ids in horror list
for id in horror_ids:
    horror_index[id] = 0
while queue:
    v = queue.popleft()
    for u in G[v]:
        if horror_index[u] == math.inf:
            horror_index[u] = horror_index[v] + 1
            queue.append(u)

smallest_unreachable = None
for id in range(N):
    if horror_index[id] == math.inf:  # Unreachable
        if smallest_unreachable is None or id < smallest_unreachable:
            smallest_unreachable = id

# If no unreachable movies, find the highest Horror Index
if smallest_unreachable is None:
    highest = 0
    for id in range(1, N):
        if horror_index[id] > horror_index[highest] or (horror_index[id] == horror_index[highest] and id < highest):
            highest = id
    print(highest)
else:
    print(smallest_unreachable)
