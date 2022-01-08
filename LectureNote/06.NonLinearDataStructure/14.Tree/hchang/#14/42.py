# 이진트리의 최대깊이를 구하여라
# [3, 9, 20, null, null, 15, 7]
# 정답: 3
# 이런식!

from BinaryTree import TreeNode



null = "null"

tree = [3,9,20, null, null, 15,7]


root = TreeNode(tree)
root.print_tree()

task = [root]
now_task = []
count = 0
while task:
    print(task)
    now_task = task
    task = []
    count += 1
    for i in now_task:
        if i.right and i.right.val != 'null':
            task.append(i.right)
        if i.left and i.left.val != 'null':
            task.append(i.left)

print(count)
    

def solution():
    ...




