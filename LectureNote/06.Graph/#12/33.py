# 2에서 9까지 숫자가 주어졌을때, 조합가능한 모든 숫자 출력
# ?! 이런 억지 문제 풀기 싫은데...?

하 = {
    2:('a','b','c'),
    3:('d','e','f'),
    4:('g','h','i'),
    5:('j','k','l'),
    6:('m','n','o'),
    7:('p','q','r','s'),
    8:('t','u','v'),
    9:('w','x','y','z')
}

# _input = "23"
# num = map(int,_input)
# alpha = []
# for i in num:
#     alpha.append(하[i])

# answer = []
# for i in 하[_input[0]]:
#     answer.append(i)
# def dfs(now):
#     lst = []
#     if now in len(_input):
#         alpha[now]


# for i in alpha:
#     for j in i:



def letter(digits):
    def dfs(index, path):
        if len(path)