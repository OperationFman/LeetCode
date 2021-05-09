class Solution:
    def removeDuplicates(self, nums):
        """ [1,1,2] """
        nums = list(set(nums)) # Convert to a set which makes everything unique, back to a list
        

class Solution2: # if asked to edit in place
    def removeDuplicates(self, nums):
        """ [1,1,2] """
        nums[:] = sorted(set(nums)) # nums[:] actually creates a copy, by turning it into a set and resorting it's legit
        return len(nums)