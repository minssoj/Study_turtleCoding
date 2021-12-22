s = "abcabcbb"

def lengthOfLongestSubstring(s):
    
    used = {}
    
    max_length = start = 0
    
    for index, char in enumerate(s): # s 를 enumerate로 index 와 char에 하나씩 꺼냅니다. 
        # 이미 등장했던 문자라면 `start` 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:  # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)

        # 현재 문자의 위치 삽입
        used[char] = index # char 에 해당하는 index 를 dictionary에 저장하고, char 가 이미 dictionary에 저장 되어 있으면 중복문자입니다.  

    return max_length

print(lengthOfLongestSubstring(s))
