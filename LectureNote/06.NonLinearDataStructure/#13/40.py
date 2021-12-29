# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
# (u,v,w)는 출발지, 도착지, 소요시간 N 은 전체 노드 개수
import heapq

times = [[2,1,1],[2,3,1],[3,4,1]]
N, K = 4, 2

task = []

time = [0]*(N+1)

graph = [[] for i in range(N+1)]


for i in times:
    graph[i[0]].append(tuple(i[1:]))    

task.extend(graph[K])
while task:
    a = task.pop(0)
    if time[a[0]] == 0 or time[a[0]] > a[1]:
        time[a[0]] = a[1]
        for i in graph[a[0]]:
            task.append((i[0],i[1]+a[1]))


print(graph)
print(time)
print(max(time))
    


