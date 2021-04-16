class Solution:
    def subsets(self, nums):
        result = [[]]
        for i in nums:
            for j in range(len(result)):
                cursor = result[j] + [i]
                result += cursor,
        return result

# All good to copy, no idea why that final cursor has an ',' after it