# put(key, value): 해시 연결, 이미 존재한다면 업데이트
# get(key): 키에 해당 값 조회, 없으면 -1
# remove(key): 키에 해당하는 해시 삭제
from time import time
from My_Structure import ListNode



class MyHashMap:
    def __init__(self):
        self.key = ListNode(ListNode(-1))
        self.key.next = ListNode(ListNode(None))
    
    def put(self, key, value):
        node = self.key
        while node.next:
            if node.val.val == key:
                node.val.next = ListNode(value)
                return None
            node = node.next
        node.val = ListNode(key)
        node.val.next = ListNode(value)
        node.next = ListNode(ListNode(None))
        return None

    def get(self, key):
        node = self.key
        while node:
            if node.val.val == key:
                return node.val.next.val
            node = node.next
        return -1

    def remove(self, key):
        node = self.key
        while node:
            if node.val.val == key:
                prev.next = node.next 
            prev = node
            node = node.next



hashmap = MyHashMap()
hashmap.put(3,10)
hashmap.put(2,3)
hashmap.put(5,3)
hashmap.put(1,7)
hashmap.put(5,2)
hashmap.put(5,2)
for i in range(10000):
    hashmap.put(i+10, 1)



print(hashmap.get(3))
hashmap.remove(2)
print(hashmap.get(2))
print(hashmap.get(5))
st = time()
print(hashmap.get(3))
print(time() - st)

st = time()
print(hashmap.get(10000))
print(time() - st)

