class Solution:
    def twoSum(self, nums, target):
        for i, v in enumerate(nums): # Go through each value
            for j, k in enumerate(nums): # Check that value against all the others, but uhoh, what if it checks itself and gets the target?
                if v + k == target and j != i: # If the values equal the target AND arnt the same spot in the list
                    return [i, j] # Return them