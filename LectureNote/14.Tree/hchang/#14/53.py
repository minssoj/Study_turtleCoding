

from BinaryTree import TreeNode
null = 'null'
tree1 = [4,2,6,1,3,null,null]
tree2 = [10,4,15,1,8,null,null]

root = TreeNode(tree2)

root.print_tree()

lst = root.inorder()

print(lst)

minnum = -1
prenum = None
for i in lst:
    if prenum is None:
        prenum = i.val
        continue
    if type(i.val) is int and minnum == -1:
        minnum = abs(i.val - prenum)
        prenum = i.val
        continue
    if type(i.val) is int and minnum > abs(i.val - prenum):
        minnum = abs(i.val - prenum)
    if type(i.val) is int: prenum = i.val

print(minnum)

# df = []
# def dif(root):
#     num = root.val

    
#     dif(root.left)

#     dif(root.right)