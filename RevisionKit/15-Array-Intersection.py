from collections import Counter # Counter is used to make things cleaner

class Solution:
    def intersect(self, nums1, nums2):
        """ nums1 = [1,2,2,1], nums2 = [2,2] """
        count = Counter(nums1) # Counts all the occurances of each. [1: 2, 2: 2] 1 twice and 2 twice
        result = []
        
        for i in nums2: # Iterate through the other list [2, 2]
            if count[i] > 0: # If the value in said list is more than 1 in the count it means there's an intersection
                # e.g 2 is in the count
                result.append(i) # Add it to the list
                count[i] -= 1 # Count down the intersection because it's been 'used' count = [1: 2, 2: 1]
                
        return result