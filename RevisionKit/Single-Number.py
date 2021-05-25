class Solution:
    def singleNumber(self, nums):
        for i, v in enumerate(nums): # Get an index/value pair for each in the list
            """ [2,2,1,4,4] """
            nums.pop(i) # 1. Remove by index, e.g. index 0 (the first '2')
            if v not in nums:  # 2. Check if 2 is still in the list [2,1,4,4]. It is, so it skips
                return v # 4. When 1 is removed it can't be found in the list, so is returned
            nums.insert(i, v) # 3. Put 2 back in the list at index 0