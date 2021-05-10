class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tree = [] # The result is a list, this will store it outside the methods
    
    def inorderTraversal(self, root):
        if root != None: # Check if the binary tree is empty first, if it isn't then start recursion
            self.view(root) #Insert the entire tree
        return self.tree
            
    def view(self, cur):
        if cur != None: # Check if it's not the end of a branch
            self.view(cur.left) # Run all the lefts first
            self.tree.append(cur.val) # Move backwards up the lefts printing the values
            self.view(cur.right) # Move down all the rights as we go
            # At the end it will do all the rights and print their values

            #Self.tree is returned after all the rcursion is done above this method