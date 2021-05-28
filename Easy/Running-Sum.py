class Solution:
    def runningSum(self, nums):
        result = []
        runner = 0
        for i in nums:
            runner += i
            result.append(runner)
        return result