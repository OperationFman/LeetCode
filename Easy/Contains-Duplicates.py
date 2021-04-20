class Solution:
    def containsDuplicate(self, nums):
        for index, value in enumerate(nums):
            nums.pop(index)
            if value in nums:
                return True
            nums.insert(index, value)
        return False

    def containsDuplicate2(self, nums):
        if len(set(nums)) != len(nums):
            return True
        return False