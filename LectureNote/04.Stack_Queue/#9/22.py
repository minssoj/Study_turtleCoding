# hchang
T = [73,74,75,71,69,72,76,73]
hotday = []
for i,j in enumerate(T):
    wait = 0
    for k,l in enumerate(T):
        if j < l and i < k:
            wait = k-i
            break
    hotday.append(wait)
print(hotday)


# yeonkkk
# 일일 온도 
# 매일의 화씨 온도(F) 리스트 T를 입력받아서, 
# 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야하는지 출력하라.
T = [73, 74, 75, 71, 69, 72, 76, 73] # 출력 [1, 1, 4, 2, 1, 1, 0, 0]

# 스택 값 비교
def solution(T):
    answer = [0] * len(T) # 일자 순서대로 더 따뜻한 날씨를 기록
    stack = [] # 각 일자의 인덱스를 담는 리스트 (인덱스의 차 -> 날짜의 차)
    for i, cur in enumerate(T):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        # T[stack[-1]]: 전 날 온도
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    
    return answer

print(solution(T))
