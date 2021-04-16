# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root != None:
            return self._height(root, 0)
        else:
            return 0
        
    def _height(self, cur, cur_height):
        if cur == None:
            return cur_height
        leftH = self._height(cur.left, cur_height + 1)
        rightH = self._height(cur.right, cur_height + 1)
        return max(leftH, rightH)

# Don't Refactor
# Root appears as:
#TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
