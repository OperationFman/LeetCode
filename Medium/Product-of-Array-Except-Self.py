import numpy # 

class Solution:
    def productExceptSelf(self, nums):
        result = []
        for i, v in enumerate(nums):
            nums.pop(i)
            result.append(numpy.prod(nums))
            nums.insert(i, v)
        return result