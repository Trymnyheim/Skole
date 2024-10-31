import sys

def main():
    v = AVLTree()
    commands = sys.stdin.read().splitlines()
    n = commands[0]
    for command in commands[1:]:
        if command == "size":
            print(v.size())
        else:
            operation, n = command.split(" ")
            n = int(n)
            if operation == "contains":
                print(v.contains(n))
            if operation == "insert":
                v.insert(n)
            if operation == "remove":
                v.remove(n)


class AVLTree:
    def __init__(self):
        self.root = None

    def contains(self, x):
        if self.root == None:
            return False
        else:
            return self.root.contains(x)

    def insert(self, x):
        if self.root == None:
            self.root = AVLNode(x)
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


class AVLNode:
    def __init__(self, element = None):
        self.left = None
        self.right = None
        self.element = element
        self._size = 1
        self._height = 1

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

    def height(self):
        if self == None:
            return -1
        return self._height
        
    def setHeight(self):
        if self.left == None:
            leftHeight = 0
        else:
            leftHeight = self.left.height()
        if self.right == None:
            rightHeight = 0
        else:
            rightHeight = self.right.height()
        self._height = max(leftHeight, rightHeight) + 1


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
                self.left = AVLNode(x)
            else:
                self.left = self.left.insert(x)
        elif x > self.element:
            if self.right == None:
                self.right = AVLNode(x)
            else:
                self.right = self.right.insert(x)
        self.setSize()
        self.setHeight()
        return self.balance()

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
        self.setHeight()
        return self.balance()

    def FindMin(self):
        if self.left != None:
            return self.left.FindMin()
        else:
            return self
        
    def leftRotate(self):
        y = self.right
        t = y.left
        y.left = self
        self.right = t
        self.setSize()
        y.setSize()
        self.setHeight()
        y.setHeight()
        return y


    def rightRotate(self):
        y = self.left
        t = y.right
        y.right = self
        self.left = t
        self.setSize()
        y.setSize()
        self.setHeight()
        y.setHeight()
        return y

    def balanceFactor(self):
        if self == None:
            return 0
        if self.left == None:
            leftHeight = 0
        else:
            leftHeight = self.left.height()
        if self.right == None:
            rightHeight = 0
        else:
            rightHeight = self.right.height()
        return leftHeight - rightHeight

    def balance(self):
        if self.balanceFactor() < -1:
            if self.right.balanceFactor() > 0:
                self.right = self.right.rightRotate()
            return self.leftRotate()
        if self.balanceFactor() > 1:
            if self.left.balanceFactor() < 0:
                self.left = self.left.leftRotate()
            return self.rightRotate()
        return self


if __name__ == "__main__":
    main()
