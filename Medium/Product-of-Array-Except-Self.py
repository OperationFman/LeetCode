import numpy # Has a method that allows acquiring the product of a list

class Solution:
    def productExceptSelf(self, nums):
        result = []
        for i, v in enumerate(nums): #Classic, remove item from list, do action on the list, put it back
            nums.pop(i)
            result.append(numpy.prod(nums))
            nums.insert(i, v)
        return result