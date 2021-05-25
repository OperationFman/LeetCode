# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as 
# it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1, nums2):
        """ nums1 = [1,2,2,1], nums2 = [2,2] """
        # Clue: Use counter and decrement as you iterate. Thus O(n)