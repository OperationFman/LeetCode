class Solution:
    def singleNumber(self, nums):
        for i in nums:
            index = nums.index(i)
            nums.pop(index)
            if i not in nums:
                return i
            nums.insert(index, i)

sol = Solution()
print(sol.singleNumber([1,2,2]))
print(sol.singleNumber([1,2,3,4,5,4,3,2,1]))
print(sol.singleNumber([1,40,40,9,1]))