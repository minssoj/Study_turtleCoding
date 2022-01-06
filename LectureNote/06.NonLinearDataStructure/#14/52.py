# 이진탐색 트리(BST)가 주어졌을 때, L 이상 R 이하의 값을 지닌 노드의 합을 구하여라.

from collections import deque



null = 'null'
tree = ['A','B','C','D','E','F','G','H']

class TreeNode:
    def __init__(self, data, right=None, left=None):
        self.right = right
        self.left = left
        if type(data) is list:
            self.val = None
            self.insert_list(data)
        else:
            self.val = data

    def __str__(self):
        return f"{self.val}"

    def inorder(self):
        if self.right==None and self.left==None:
            return print(self)
        else:
            if self.left!=None:
                self.left.inorder()
            print(self)
            if self.right!=None:
                self.right.inorder()
        
    def preorder(self):
        if self.right==None and self.left==None:
            return print(self)
        else:
            print(self)
            if self.left!=None:
                self.left.preorder()
            if self.right!=None:
                self.right.preorder()

    def postorder(self):
        if self.right==None and self.left==None:
            return print(self)
        else:
            if self.left!=None:
                self.left.postorder()
            if self.right!=None:
                self.right.postorder()
            print(self)

    def breadth_first_search_list(self):
        now_list = []
        task = deque([self])
        while task:
            node = task.popleft()
            now_list.append(node)
            if node.left:
                task.append(node.left)
            if node.right:
                task.append(node.right)
        return now_list

    def insert_list(self, lst):
        branchs = deque([self])
        while branchs:
            try:
                branch = branchs.popleft()
                if branch.val==None:
                    i = lst.pop(0)
                    branch.val = i
                    branchs.append(branch)
                    continue
                if branch.left==None:
                    i = lst.pop(0)
                    branch.left=TreeNode(i)
                    branchs.append(branch.left)
                if branch.right==None:
                    i = lst.pop(0)
                    branch.right=TreeNode(i)
                    branchs.append(branch.right)
            except IndexError:
                print("all do that")
                break
                


root=TreeNode(tree)





# root.postorder()
# print(root.right)

now_list = root.breadth_first_search_list()
for i in now_list:
    print(i)
