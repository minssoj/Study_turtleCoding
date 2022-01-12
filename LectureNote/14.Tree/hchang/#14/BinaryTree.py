from collections import deque
import math


# null = 'null'
# tree = [4,1,3,6,2,7,5,2,6,8,100]

class TreeNode:
    def __init__(self, data, right=None, left=None, normal=True):
        self.right = right
        self.left = left
        if type(data) is list and normal:
            self.val = None
            self.insert_list(data)
        else:
            self.val = data

    def __repr__(self):
        return f"{self.val}"

    def find_max(self):
        ...

    def inorder(self,lst = []):

        if self.right==None and self.left==None:
            lst.append(self)
            # print(self)
        else:
            if self.left!=None:
                self.left.inorder(lst)
            lst.append(self)
            # print(self)
            if self.right!=None:
                self.right.inorder(lst)
        return lst

        
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

    def print_tree(self):
        lst = self.breadth_first_search_list()
        N = len(lst)
        power2 = [1,2]
        def log2(num):
            return math.log2(num)
        count = 0
        for i,j in enumerate(lst):
            good = 72//(2**count+1)
            if i+1 in power2:
                print(' '*good, end='')
            print(j,end=' '*(good-len(str(j))))
            if log2(N) >= i:
                power2.append(2**i)
            if i+2 in power2:
                print('\n')
                count += 1

        print('\n')
                


# root=TreeNode(tree)

# root.print_tree()



# root.postorder()
# print(root.right)

# now_list = root.breadth_first_search_list()
# for i in now_list:
#     print(i)
# root.print_tree()