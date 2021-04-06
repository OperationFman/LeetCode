class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in nums:
            remainder = target - i
            if remainder in nums and nums.index(i) != nums.index(remainder):
                result.append(nums.index(i))
                result.append(nums.index(remainder))
                return result
        if result == []:
            for j in nums:
                index = nums.index(j)
                store = nums.pop(nums.index(j))
                remainder = target - store
                for _ in nums:
                    if remainder in nums:
                        result.append(index)
                        result.append(nums.index(remainder) + 1)
                        return result
                nums.insert(index, store)

solution = Solution()
array = [3, 2, 3]
solution.twoSum(array, 6)