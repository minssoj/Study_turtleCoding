# 이진트리의 최대깊이를 구하여라
# [3, 9, 20, null, null, 15, 7]
# 정답: 3
# 이런식!

null = "null"

tree = [3,9,20, null, null, 15,7]

class TreeNode:
    def __init__(self, data, right=None, left=None):
        self.val = data
        self.right = right
        self.left = left

    def print_all():
        ...

root=TreeNode(None)



branchs = [root]
while branchs:
    try:
        branch = branchs.pop(0)
        if root.val==None:
            i = tree.pop(0)
            root = TreeNode(i)
            branchs.append(root)
            continue
        if branch.left==None:
            i = tree.pop(0)
            branch.left=TreeNode(i)
            branchs.append(branch.left)
        if branch.right==None:
            i = tree.pop(0)
            branch.right=TreeNode(i)
            branchs.append(branch.right)
    except IndexError:
        print("all do that")
        break



print(root.right.left.val)



