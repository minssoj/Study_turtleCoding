# from My_Structure import Stack

# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)

# print(stack.pop())

from time import time
from collections import deque
a = [12]*10000
b = deque([12])*10000
st = time()
a.pop()
print(time()-st)
st = time()
a.pop(0)
print(time()-st)
st = time()
b.pop()
print(time()-st)
st = time()
b.popleft()
print(time()-st)