from collections import deque
import sys

def main():
    teque = Teque()
    commands = sys.stdin.read().splitlines()
    n = commands[0]
    for line in commands[1:]:
        operation, num = line.split(" ")
        num = int(num)
        if operation == "push_back":
            teque.push_back(num)
        if operation == "push_front":
            teque.push_front(num)
        if operation == "push_middle":
            teque.push_middle(num)
        if operation == "get":
            print(teque.get(num))


class Teque:
    def __init__(self):
        self.left = deque()
        self.right = deque()
    
    def push_back(self, x):
        self.right.append(x)
        self.checkBalance()

    def push_front(self, x):
        self.left.appendleft(x)
        self.checkBalance()

    def push_middle(self, x):
        self.left.append(x)
        self.checkBalance()

    def get(self, i):
        mid = len(self.left)
        if i >= mid:
            return self.right[i - mid]
        else:
            return self.left[i]

    def checkBalance(self):
        if len(self.left) < len(self.right):
            self.left.append(self.right.popleft())
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())


if __name__ == "__main__":
    main()

        

