# 스텍을 이용한 큐 구현

class Myqueue:
    def __init__(self):
        self.st = list()

    def push(self, item):
        self.st.append(item)


    def pop(self):
        return self.st[::-1].pop()

    def peek(self):
        return self.st[0]

        