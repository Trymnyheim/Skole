# https://open.kattis.com/problems/teque

from collections import deque
from sys import stdin

def main():
    # Reading input:
    n = int(next(stdin))
    commands = []
    for _ in range(n):
        command = next(stdin).strip().split()
        commands.append(command)
    
    # Initiziate queue
    teque = Teque()

    # Performs operations in commands:
    for com in commands:
        operation, num = com
        num = int(num)
        if operation == "push_back":
            teque.push_back(num)
        if operation == "push_front":
            teque.push_front(num)
        if operation == "push_middle":
            teque.push_middle(num)
        if operation == "get":
            print(teque.get(num))


# Consits of two deques for O(1) enqueueing at start, middle and end
class Teque:
    def __init__(self):
        self._left = deque()
        self._right = deque()
    
    # Inserts x in the back of teque
    def push_back(self, x):
        self._right.append(x)
        self._checkBalance()

    # Inserts x in the front of teque
    def push_front(self, x):
        self._left.appendleft(x)
        self._checkBalance()

    # Inserts x in the middle of teque
    def push_middle(self, x):
        self._left.append(x)
        self._checkBalance()

    # Returns the i-th element of the teque
    def get(self, i):
        mid = len(self._left)
        if i >= mid:
            return self._right[i - mid]
        else:
            return self._left[i]

    # Ensures that the balance between each deque is good
    def _checkBalance(self):
        if len(self._left) < len(self._right):
            self._left.append(self._right.popleft())
        if len(self._left) > len(self._right) + 1:
            self._right.appendleft(self._left.pop())

if __name__ == "__main__":
    main()

        

