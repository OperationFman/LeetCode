nums1 = [1,2,2,1]
nums2 = [2,2]


def intersect(self, nums1, nums2):
        res = []
        p1 = 0
        p2 = 0
            
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
                
        return res

# Refactor!!
# Output: [4,9]