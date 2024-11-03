# https://open.kattis.com/problems/numbertree

from sys import stdin

def main():
    inp = next(stdin)
    try:
        H, directions = inp.strip().split()
    except ValueError:
        # Input contained no directions
        H = inp
        directions = None
    H = int(H) # Height of tree
    size = find_size(H) # Amount of nodes in tree relativ to H
    if directions:
        print(size - find_node_index(directions))
    else:
        print(size)
    

def find_node_index(directions):
    # index of root node is 0
    i = 0
    for dir in directions:
        if dir == "L": # i replaced with index of left child
            i = left_of(i)
        if dir == "R": # Same with right child
            i = right_of(i)
    return i


# Returns index of left child
def left_of(i):
    return i*2 + 1


# Returns index of right child
def right_of(i):
    return i*2 + 2


# Returns node size of tree from height
def find_size(height):
    val = 1
    for i in range(height):
        val += 2**(i+1)
    return val

if __name__ == "__main__":
    main()