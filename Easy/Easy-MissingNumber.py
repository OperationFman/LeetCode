class Solution:
    def missingNumber(self, nums):
        bigList = []
        for i in range(999999):
            bigList.append(i)
        for j in bigList:
            if j not in nums:
                return j