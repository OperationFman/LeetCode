class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Copy array and chop off everything after n
        # From n to the end of the original, increment a counter by 2 and insert in the original array
        copy = nums.copy()
        shuffle = []
        
        for i in range(n):
            shuffle.append(nums.pop(0))
            
        count = 1
        
        for i in nums:
            shuffle.insert(count, i)
            count += 2
            
        return shuffle