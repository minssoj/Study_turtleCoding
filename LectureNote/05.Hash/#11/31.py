# 상위 K빈도 요소
# 입력
num = [1,1,1,2,2,3]
k = 2
# 출력
# 빈도 수 k위까지 리스트로 출력

from collections import Counter
import heapq as hp
from time import time





st = time()
counter = Counter(num)
print(sorted(counter,key=lambda x: counter[x],reverse=True)[:2])
print(time() - st)





st = time()
ct = Counter(num)
answer=[]
heaplst = [(-j,i) for i,j in ct.items()]
hp.heapify(heaplst)

for i in range(2):
    answer.append(hp.heappop(heaplst)[1])
print(answer)

print(time()-st)










st = time()

counter = Counter(num)
print([i[0] for i in counter.most_common(2)])
print(list(zip(*counter.most_common(2)))[0])


print(time() - st)
