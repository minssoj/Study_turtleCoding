# 1육지로 0을 물로 가정한 2D 그리드 맵
# 섬의 개수를 구하여라.

import sys
sys.stdin = open('data/32-1.txt', 'r')

graph = []
for i in sys.stdin.readlines():
    graph.append(list(map(int, list(i.strip()))))

height = len(graph)
width = len(graph[0])

# ---------------------- dfs로 풀기-----------------------

def find_adja(now):
    lst = []
    a,b = now
    lst.append((a-1,b))
    lst.append((a+1,b))
    lst.append((a,b-1))
    lst.append((a,b+1))
    return lst

def dfs_cha(now, task=[]):
    task.append(now)
    for a,b in task:
        if a in range(height) and b in range(width) and graph[a][b] ==1:
            graph[a][b] = 2
            task.extend(find_adja((a,b)))

count = 0 

for i in range(height):
    for j in range(width):
        if graph[i][j] == 1:
            dfs_cha((i,j))
            count += 1
print(count)

# --------------------------교재 풀이 ----------------

# class Solution:
#     def dfs(self, graph, i, j):
#         # 더 이상 땅이 아닌 경우 종료
#         if i in range(height) or j in range(width) \
#             or graph[i][j] != 1:
#                 return
            
#         graph[i][j] = 0
        
#         self.dfs(graph, i+1,j)
#         self.dfs(graph, i-1,j)
#         self.dfs(graph, i, j-1)
#         self.dfs(graph, i, j+1)

#     def numIslands(self, graph):
#         if not graph:
#             return 0

#         count = 0
#         for i in range(height):
#             for j in range(width):
#                 if graph[i][j] == 1:
#                     self.dfs(graph, i,j)
#                     count += 1
#         return count

# if __name__ == '__main__':
#     print(Solution().numIslands(graph))
    
