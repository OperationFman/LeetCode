class Solution:
    def missingNumber(self, nums):
        """ [3,0,1] """
        try:
            for i in range(len(nums) + 1): # Get a range for all numbers, easily getting the index
                if i not in nums: # If it isn't in the list return it
                    return i
        except:
            return 0 # If the list is empty or nothing it would be zero, negative or positive, might aswell catch it