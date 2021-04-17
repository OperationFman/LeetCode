class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        q = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            q.append(root.val)
            inorder(root.right)
        inorder(root)
        return q[k-1]

# Refactor! Honestly no idea what's being asked here