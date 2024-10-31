# Checks if a binary tree is a search tree, O(2n)
def check_BST(v):
    if v is None:
        return None
    min, max = find_minmax(v)
    left = BST_trav(v.left, min - 1, v.element)
    right = BST_trav(v.right, v.element, max + 1)
    return left and right
    
# Traverses all nodes and makes sure the children are less/greater than parents
def BST_trav(v, min, max):
    if v is None:
        return True
    if v.element <= min or v.element >= max:
        return False
    left = BST_trav(v.left, min, v.element)
    right = BST_trav(v.right, v.element, max)
    return left and right


# Finds min and max value of a binary tree in O(n)
def find_minmax(v):
    # return [-math.inf, math.inf] # For better complexity
    min = v.element
    max = v.element
    queue = [v]
    while len(queue) != 0:
        v = queue.pop()
        if v.element < min:
            min = v.element
        if v.element > max:
            max = v.element
        if v.left:
            queue.append(v.left)
        if v.right:
            queue.append(v.right)
    return [min, max]