# https://open.kattis.com/problems/boxes

from sys import stdin
from collections import deque

def main():
    N = int(next(stdin)) # Number of boxes
    contains = [int(x) for x in next(stdin).strip().split()]

    # Build tree
    tree = build_tree(N, contains)

    # Queries:
    Q = int(next(stdin)) # Amount of queries
    output = []
    for i in range(Q):
        query = [int(x) for x in next(stdin).strip().split()]
        # Solving the problem for each query and append to output list
        solution = find_boxes(tree, query[1:]) # First n of query is not relevant
        output.append(solution)

    # Printing output
    for n in output:
        print(n)


# Creates a dict with each node as key and a set of children as value
def build_tree(N, contains):
    tree = {i + 1: set() for i in range(N)}
    for i, parent in enumerate(contains):
        if parent != 0:
            tree[parent].add(i + 1) # Adds children
    return tree


# BFS-traversal of tree, returns number of nodes reached
def find_boxes(tree, query):
    queue = deque(query)
    boxes = set()
    while queue:
        box = queue.popleft()
        if box not in boxes:
            boxes.add(box)
            queue.extend(tree[box])
    return len(boxes) # Amount of boxes found


if __name__ == "__main__":
    main()
