class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        nums_len = len(nums)
        if nums_len == 1:
            # if there's only one element in list, it will have no children
            return TreeNode(
                val = nums[0],
                left = None,
                right = None
            )
        
        mid_pt = nums_len // 2
        
        node = TreeNode(
            val = nums[mid_pt],
            left = self.sortedArrayToBST(nums[:mid_pt]),
			# if there are no values greater than root of sub-tree, right should be None
            right = self.sortedArrayToBST(nums[mid_pt+1:]) if mid_pt + 1 < nums_len else None
        )

        return node

# Refactor!