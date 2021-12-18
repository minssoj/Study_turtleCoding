class Node:
    def __init__(self, item: int, prev=None):
        self.item = item
        self.prev = prev

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.prev
        return item
