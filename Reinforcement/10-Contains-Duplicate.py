class Solution:
    def containsDuplicate(self, nums):
        try: # As always, the result is true or false so might aswell setup an exception
            result = False # 3. If the loop never reveals a duplicate value then the whole array must not have any dupes
        
            for i, v in enumerate(nums): # Need key value because we're removing items and checking the list without them
                nums.pop(i) # remove by index
                if v in nums: # 1. Check if value is still in the list
                    result = True # 2. If it is then the whole list will equal true
                nums.insert(i, v) # Put the value back, if the true value is spotted again it wont matter since result already equals true

            return result
        except:
            return False
        # This actually fails due to LeetCode being slow, exceeding time limit. But it is correct
