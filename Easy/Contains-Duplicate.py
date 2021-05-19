class Solution:
    def containsDuplicate(self, nums):
        if len(nums) != len(set(nums)): #When we make the list unique (set) it'll remove duplicates
            return True # If that's less than originally then it'll mean there was dups in it
        return False # If it's the same then it must have been unique