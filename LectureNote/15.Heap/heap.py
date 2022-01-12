# Heap.py
class Heap:
    def __init__(self, heap_type):
        self.heap = [None] #* 완전 이진트리이므로, 리스트로 구현한다. # 왜 인덱스를 1부터 활용할까? 부모 자식 노드의 인덱스 관계를 활용하기 위해
        self.size = 0
        self.heap_type = heap_type

    def push(self, item):
        #* 값을 힙에 넣는다.
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def arrange(self, k):
        #* 값을 넣을 때 마다 힙 전체를 정렬한다.
        #? k : 마지막 노드의 인덱스
        while k // 2 > 0:
            #* 인덱스를 2로 나누는 방식으로 위로 올라간다.
            if self.heap[k] < self.heap[k//2]: #* 마지막 노드의 값 부모 노드보다 작으면 swap 을 해주어야 합니다.
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2
            
    def pop(self):
        item = self.heap[1] #* 힙 트리의 루트 노드의 값을 가져온다.
        self.heap[1] = self.heap[self.size]   #* 마지막 노드의 값을 루트 노드로 가져온다.
        self.size -= 1
        self.heap.pop() #* 마지막 노드의 값을 삭제한다.
        self.sink(1) #* 루트 노드의 인덱스엣 시작해서 아래로 값을 보낸다.
        
        return item

    def minindex(self, k):
        #* k번째 노드의 자식 중에서 어떤 노드가 작은 지 비교하고 자식 인덱스를 반환한다.
        if k * 2 + 1 > self.size: #* 오른쪽 자식 노드가 존재하지 않으면
            return k * 2 #* 왼쪽 자식 노드의 인덱스를 리턴한다.
        elif self.heap[k*2] < self.heap[k*2+1]: #* 오른쪽 자식노드보다 왼쪽 자식노드가 작으면
            return k * 2
        else: # 오른쪽이 왼쪽보다 작으면
            return k * 2 + 1

    def sink(self, k):
        #* k : 부모 노드의 인덱스
        #* k번째 인덱스의 노드를 받아서 아래로 보낸다.
        while k*2 <= self.size:
            m_index = self.minindex(k)
            if self.heap[k] > self.heap[m_index]: #* 부모 노드의 값이 자식 노드의 값보다 크면, 두 노드의 값을 교환한다.
                self.heap[k], self.heap[m_index] = self.heap[m_index], self.heap[k]
            k = m_index

heap = Heap('min')
data = [3, 5, 6, 7, 9, 10, 2]
for item in data:
    heap.push(item)

#! [None, 2, 3, 5, 6, 7, 9, 10]
print(heap.heap)

heap2 = Heap('min')
for item in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    heap2.push(item)
    
for _ in range(10):
    n = heap2.pop()
    print(n)
    print(heap2.heap)