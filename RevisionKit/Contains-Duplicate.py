# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums):
        """ [1,1,2,3] """
        pass
        # Clue: it's a boolean return
        # Clue: If a list was converted to a set, and it had a duplicate, it would be shorter than the original list
        return len(set(nums)) != len(nums)
