class BinaryTree:
    def __init__(self):
        self.root = None

    def contains(self, x):
        if self.root == None:
            return False
        else:
            return self.root.contains(x)

    def insert(self, x):
        if self.root == None:
            self.root = TreeNode(x)
        else:
            self.root = self.root.insert(x)

    def remove(self, x):
        if self.root == None:
            return None
        else:
            self.root = self.root.remove(x)

    def size(self):
        if self.root == None:
            return -1
        return self.root.size()


class TreeNode:
    def __init__(self, element = None):
        self.left = None
        self.right = None
        self.element = element
        self._size = 1

    def size(self):
        return self._size

    def setSize(self):
        if self.left == None:
            leftSize = 0
        else:
            leftSize = self.left.size()
        if self.right == None:
            rightSize = 0
        else:
            rightSize = self.right.size()
        self._size = leftSize + rightSize + 1

    def contains(self, x):
        if self.element == None:
            return False
        if x == self.element:
            return True
        elif x < self.element:
            if self.left == None:
                return False
            else:
                return self.left.contains(x)
        elif x > self.element:
            if self.right == None:
                return False
            else:
                return self.right.contains(x)

    def insert(self, x):
        if self.element == None:
            self.element = x
        elif x < self.element:
            if self.left == None:
                self.left = TreeNode(x)
            else:
                self.left = self.left.insert(x)
        elif x > self.element:
            if self.right == None:
                self.right = TreeNode(x)
            else:
                self.right = self.right.insert(x)
        self.setSize()
        return self

    def remove(self, x):
        if self.element == None:
            return None
        if x < self.element:
            if self.left:
                self.left = self.left.remove(x)
        elif x > self.element:
            if self.right:
                self.right = self.right.remove(x)
        else:
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left
            u = self.right.FindMin()
            self.element = u.element
            self.right = self.right.remove(u.element)
        self.setSize()
        return self

    def FindMin(self):
        if self.left != None:
            return self.left.FindMin()
        else:
            return self
