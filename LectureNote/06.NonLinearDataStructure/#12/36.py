# 조합의 합
candidates = [2,3,5]
target = 8

answer = []
eliment = []

def dfs():
    a = sum(eliment)
    if a == target:
        eliment.sort()
        if eliment in answer:
            return
        answer.append(eliment[:])
        return
    
    if a > target:
        return
    
    for i in candidates:
        eliment.append(i)
        dfs()
        eliment.pop()

dfs()
print(answer)

