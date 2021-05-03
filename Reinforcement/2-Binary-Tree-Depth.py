class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root): # The tree is already passed in as the below green text
        """ TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, 
            right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, 
            right: TreeNode{val: 7, left: None, right: None}}} """
        if root != None:                 # Starts the following method with 0.
            return self._height(root, 0) # The result with be a single int of the longest branch.
        else:
            return 0 #Edge Case: Could be empty, so 0.
        
    def _height(self, cur, cur_height): #2. Left node is now main node, height incremented by 1
        if cur == None: # 3. Node could be last one so return the height
            return cur_height
        left_height = self._height(cur.left, cur_height + 1) # 1. Passes in remaining tree from left node
        right_height = self._height(cur.right, cur_height + 1) # 4. Runs aswell, all branches will be travelled
        return max(left_height, right_height) # Will return current longest, when moving up itll report the enxt longest etc
        # Works all the way back upto the first left & right nodes with longest branch only