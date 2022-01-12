# TODO : count_height 함수 작성
# 1. 재귀함수를 돌면서 height를 더해 나가면서 저장
# 2. 딕셔너리를 통해 키 : 노드, 벨류 : 높이를 저장
# 3. 함수의 입력 : 노드의 개수 n, 간선 집합 edges


def count_minimum_height():
    pass

import collections

edges = [[1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [6, 10], [5, 7], [5, 8], [8, 9]]

# ! 꼭 노드를 없애면서 문제를 풀어야할까?
# ! 노드를 탐색하면서 다음 노드가 없을 때까지 탐색하는 방법은 안될까?
def findMinHeightRees(n, edges):
    if n <= 1:
        return [0]
    
    graph = collections.defaultdict(list) # 딕셔너리 키 : 노드, 벨류 : 인접리스트
    for i, j in edges:
        # 그래프가 무방향이므로 양쪽 노드에 모두 연결된 노드를 추가한다.
        graph[i].append(j)
        graph[j].append(i)
        
        # 딕셔너리의 벨류값이 연결된 노드 리스트이므로 이 길이를 센다.
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)

    print(graph)    
    while n > 2:
        n -= len(leaves)
        # * new_leaves가 왜 필요할까?
        # FIXME :
        # TODO :
        
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
    
        leaves = new_leaves
        
    print(graph)    
    return leaves
leaves = findMinHeightRees(10, edges)
print(leaves)