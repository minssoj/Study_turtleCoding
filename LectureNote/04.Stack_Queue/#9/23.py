from collections import deque


class Mystack:
    def __init__(self):
        self.q = deque()

    def push(self, item):
        self.q.append(item)

    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q[-1]

    def empty(self):
        return not bool(self.q)

stack = Mystack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())