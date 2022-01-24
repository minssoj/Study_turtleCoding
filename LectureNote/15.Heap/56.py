
# 트라이를 저장할 노드 선언
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
    
# 트라이 연산을 구현할 클래스 선언
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    # 단어 탐색
    def search(self, word): # word 전체가 있는지 확인
        node = self.root
        for char in word: # 'apple'
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word # 완성된 단어면 True 리턴

    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True



# 입력 값
t = Trie()
t.insert('apple')
# t.insert('appear')
# t.insert('appeal')
print(t.search('apple')) # true
print(t.search('app')) # false
print(t.startsWith('app')) # true
t.insert('app')
print(t.search('app')) # true

            

