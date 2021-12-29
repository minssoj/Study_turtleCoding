# 전체 수 n을 입력받아 k개의 조합을 만들어라

from time import time


n = 6 
k = 4

answer = []
eliment = []
st = time()
def dfs(start):
    if len(eliment) == k:
        answer.append(eliment[:])
        return

    for i in range(start, n+1):
        eliment.append(i)
        start += 1
        dfs(start)
        eliment.pop()

dfs(1)

print(answer)
print(time() -st)


import itertools
st = time()
def combine(n,k):
    return list(itertools.combinations(range(1,n+1),k))

answer = combine(6,4)

print(answer)
print(time()-st)