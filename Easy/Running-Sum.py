class Solution:
    def runningSum(self, nums):
        result = []
        runner = 0 # Quicker to capture a total to add to rather than recalc the sum every time

        for i in nums:
            runner += i # Increment the runner to get the new value
            result.append(runner) # Add that value to the array
        return result