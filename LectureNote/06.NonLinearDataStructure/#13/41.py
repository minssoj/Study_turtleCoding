# 시작점에서 도착점까지 가장 저렴한 가격을 계산

# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0 # 시작 노드
# dst = 2 # 도착 노드
# K = 0 # 경유 제한 개수

# graph = [[] for i  in range(n + 1)]

# for i in edges:
#     graph[i[0]].append(tuple(i[1:]))



# ---------------

# task = []
# price = [0]*(n+1)

# def dfs(now):

#     task.extend(graph[now])
#     while task:
#         a = task.pop()
#         if price[a[0]]==0 or price[a[0]] > a[1]:
#             price[a[0]] = a[1]
#             for i in graph[a[0]]:
#                 task.append((i[0],i[1]+a[1]))




# dfs(0)
# dfs(src)
# print(price[dst])

# ----------------------k개 구현----------------------
from time import time
import random


n = 100
# ------------data generation ----------------

# with open('data/41.txt','w') as f:
#     for i in range(1000):
#         a,b,c = random.randint(0,100),random.randint(0,100),random.randint(0,500)
#         f.write(' '.join(map(str,[a,b,c]))+'\n')

import sys

sys.stdin = open("data/41.txt",'r')
edges = []
for i in range(1000):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append([a,b,c])


st = time()

# n = 7
# edges = [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,2,50],[3,6,10],[6,5,40],[6,4,100],[6,2,20]]


src = 0 # 시작 노드
dst = 2 # 도착 노드
K = 200 # 경유 제한 개수

graph = [[] for i  in range(n + 1)]

for i in edges:
    graph[i[0]].append(tuple(i[1:]))


price = [0]*(n+1)



def k_dfs(now, cost=0, k=0, task=[]):
    if k > K:
        return
    for i in graph[now]:
        # 그래프에서 요금 받아서 이전요금 더하기
        node, cst = i[0], i[1] + cost
        now_price = price[node] # 기존 요금 확인
        if now_price==0 or now_price > cst:
            price[node] = cst
            # 그 노드까지 든 요금과, 노드 번호 함수에 넣음
            k_dfs(node, cst, k+1)
        
k_dfs(src)

print(graph)

print("DFS!")
print(price)

print(price[dst])
print(time() -st)


# -----------------다익스트라-------------------
st = time()
# n = 7
# edges = [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,2,50],[3,6,10],[6,5,40],[6,4,100],[6,2,20]]
src = 0 # 시작 노드
dst = 2 # 도착 노드
# K = 1 # 경유 제한 개수

graph = [[] for i  in range(n + 1)]

for i in edges:
    s,t,c = i
    graph[s].append((c,t,0))




task = []
price = [0]*(n+1)



def k_Dijkstra(now):
    task.extend(graph[now])
    while task:
        cost, node, k = task.pop()
        if k > K:
            continue

        now_price = price[node]
        if now_price==0 or now_price > cost:
            price[node] = cost
            for ct, nd, _ in graph[node]:
                task.append((ct+cost, nd, k+1))
            
k_Dijkstra(src)
# print(graph)
print("Dijkstra!")
print(price)

print(price[dst])
print(time()-st)


# -------------------min Dijkstra-----------------------

st = time()
# n = 7
# edges = [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,2,50],[3,6,10],[6,5,40],[6,4,100],[6,2,20]]
src = 0 # 시작 노드
dst = 2 # 도착 노드
# K = 1 # 경유 제한 개수

graph = [[] for i  in range(n + 1)]

for i in edges:
    s,t,c = i
    graph[s].append((c,t,0))





task = []
price = [0]*(n+1)



def k_Dijkstra(now, k=0):
    task.extend(graph[now])
    task.sort(reverse=True)
    while task:
        cost, node, k = task.pop()
        if k > K:
            continue

        now_price = price[node]
        if now_price==0 or now_price > cost:
            price[node] = cost
            for ct, nd, _ in graph[node]:
                task.append((ct+cost, nd, k+1))
            
k_Dijkstra(src)
# print(graph)
print("min_Dijkstra")
print(price)

print(price[dst])
print(time()-st)


# -------------------heap Dijkstra-----------------------
import heapq as hq

st = time()
# n = 7
# edges = [[0,1,100],[1,2,100],[0,2,500],[0,3,10],[3,2,50],[3,6,10],[6,5,40],[6,4,100],[6,2,20]]
src = 0 # 시작 노드
dst = 2 # 도착 노드
# K = 1 # 경유 제한 개수

graph = [[] for i  in range(n + 1)]

for i in edges:
    s,t,c = i
    graph[s].append((c,t,0))





task = []
price = [0]*(n+1)



def kheap_Dijkstra(now, k=0):
    for i in graph[now]:
        hq.heappush(task,i)

    while task:
        cost, node, k = hq.heappop(task)
        if k > K:
            continue

        now_price = price[node]
        if now_price==0 or now_price > cost:
            price[node] = cost
            for ct, nd, _ in graph[node]:
                hq.heappush(task,(ct+cost, nd, k+1))
            

kheap_Dijkstra(src)
print("Heap!")
# print(graph)
print(price)

print(price[dst])
print(time()-st)
