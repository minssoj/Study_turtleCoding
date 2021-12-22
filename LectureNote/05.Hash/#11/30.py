# 중복문자 없는 가장 긴 문자열 길이 리턴
string = "abcabcbb"
counts = []
for i, j in enumerate(string):
    count = 1
    for k, l in enumerate(string[i+1:]):
        if l in string[i:k+i+1]:
            break
        count += 1
    counts.append(count)
print(max(counts))