# 2에서 9까지 숫자가 주어졌을때, 조합가능한 모든 숫자 출력
# ?! 이런 억지 문제 풀기 싫은데...?

하 = {
    2:"abc",
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

_input = "23"

answer = []
eliment = ''

def dfs(now, eliment):
    if len(eliment) == len(_input):
        answer.append(eliment)
        return

    else:
        num = int(_input[now])
        for i in 하[num]:
            dfs(now+1, eliment + i)

dfs(0, eliment)
print(answer)

        


