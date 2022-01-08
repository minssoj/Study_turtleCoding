# 이진탐색 트리(BST)가 주어졌을 때, L 이상 R 이하의 값을 지닌 노드의 합을 구하여라.

from BinaryTree import TreeNode

from time import time

null = "null"

tree = [10,5,15,3,7,null,18]
L = 7
R = 15

root=TreeNode(tree)

root.print_tree()


st = time()
lst = root.inorder()

print(lst)
answer = 0
for i in lst:
    value = i.val
    if type(value) is int and L <= value <= R:
        answer += value

print(answer)    
print(time() -st)
lst = root.breadth_first_search_list()

print(lst)
answer = 0
for i in lst:
    value = i.val
    if type(value) is int and 7 <= value <= 15:
        answer += value

print(answer)    # 일을 두번한다.


st = time()
def search_sum(root, L, R, task=[]):
    task.append(root)
    answer = 0
    while task:
        root = task.pop()
        if not root: continue
        if type(root.val) is int and L <= root.val <= R:
            answer += root.val
        if type(root.val) is int and L <= root.val:
            task.append(root.left)
            
        if type(root.val) is int and root.val <= R:
            task.append(root.right)
            
    return answer

print(search_sum(root, L, R))
print(time() -st)