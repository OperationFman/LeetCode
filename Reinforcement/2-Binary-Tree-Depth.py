class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root): # The tree is already passed in
        """ TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, 
            right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, 
            right: TreeNode{val: 7, left: None, right: None}}} """
        if root != None: 
            return self._height(root, 0)
        else:
            return 0
        
    def _height(self, cur, cur_height):
        if cur == None:
            return cur_height
        left_height = self._height(cur.left, cur_height + 1)
        right_height = self._height(cur.right, cur_height + 1)
        return max(left_height, right_height)