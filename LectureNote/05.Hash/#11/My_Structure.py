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

class ListNode:
    def __init__(self,data, next=None): 
        self.val = data
        self.next = next

    def add(self, data):
        node = self
        while node.next:
            node = node.next
        node.next = ListNode(data)

    def __getitem__(self, n):
        node = self
        if n == 0:
            return node.val
        for i in range(n):
            node = node.next
        return node.val

    def printall(self):
        node = self
        while node:
            print(node.val)
            node = node.next