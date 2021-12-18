# 데크 사이즈 k
# insertFront()
# insertLast()
# deleteFront()
# deleteLast()
# getFront()
# getRear()
# isEmpty()
# isFull()


class ListNode:
    def __init__(self,data, left=None, right=None): 
        self.val = data
        self.left = left
        self.right = right

    # def add(self, data):
    #     node = self
    #     while node.next:
    #         node = node.next
    #     node.next = ListNode(data)

    # def __getitem__(self, n):
    #     node = self
    #     if n == 0:
    #         return node.val
    #     for i in range(n):
    #         node = node.next
    #     return node.val

    # def printall(self):
    #     node = self
    #     while node:
    #         print(node.val)
    #         node = node.next

# from My_Structure import ListNode


class MyCirDeque:
    def __init__(self, k:int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head


    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int):
        if self.len ==self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int):
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))

    def deleteFront(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True


    def deleteLast(self):
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self):
        return self.head.right.val if self.len else -1

    def getRear(self):
        return self.tail.left.val if self.len else -1

    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == self.k


cirdeque = MyCirDeque(10) # 사이즈 10

print(cirdeque.isEmpty())
cirdeque.insertFront(3) # [3)
cirdeque.insertFront(4) # [34)
cirdeque.insertLast(5) # [534)
cirdeque.insertLast(6) # [6534)
cirdeque.insertLast(6) # [66534)
cirdeque.insertLast(1) # [166534)
cirdeque.insertLast(6) # [6166534)
cirdeque.insertLast(2) # [26166534)
cirdeque.insertLast(1) # [126166534)
print(cirdeque.isEmpty())
cirdeque.insertLast(7) # [71261266534)
print(cirdeque.isFull())
print(cirdeque.getFront())
print(cirdeque.deleteFront()) # [7126126653)
print(cirdeque.getFront())
print(cirdeque.deleteFront()) # [712612665)
print(cirdeque.getFront())
print(cirdeque.getRear())
