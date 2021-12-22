# S돌들 사이에 j는 보석
# 
J = "aA"
S = "aAAbbbb"
from time import time
st = time()
import re
jem = re.findall('['+ J +']',S)
print(len(jem))
print(time()-st)


def numjem(J,s):
    return sum(i in J for i in s)

st = time()
print(numjem(J,S))
print(time()-st)
