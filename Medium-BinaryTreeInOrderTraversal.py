class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if root is not None:
            listInt = []
            for x in self.inorderTraversal(root.left):
                listInt.append(x)
            listInt.append(root.val)
            for y in self.inorderTraversal(root.right):
                listInt.append(y)
            return listInt
        return []
#Refactor!!
# Root input appeared like so:
# TreeNode{val: 1, left: None, right: TreeNode{val: 2, left: TreeNode{val: 3, left: None, right: None}, right: None}}