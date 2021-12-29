# 가능한 모든 순열을 list형태로 출력하라
# *모든 배열을 뜻함
from time import time

st = time()
_input = [1,2,3,4,5]

output = []
eliment=[]

def dfs(inp):
    if len(eliment) == len(_input):
        output.append(eliment[:])
        return

    for i in inp:
        eliment.append(i)
        ninp = inp[:]
        ninp.remove(i)
        dfs(ninp)
        eliment.pop()

dfs(_input)

print(output, len(output))
print(time() -st)

st = time()
import itertools
# 2배 이상 빠르다.
def permute(_input):
    return list(itertools.permutations(_input))

output = permute(_input)
print(output, len(output))
print(time() -st)