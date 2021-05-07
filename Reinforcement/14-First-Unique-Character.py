class Solution:
    def firstUniqChar(self, s):
        s = list(s) # Can't enumerate a string, so convert to a list
        
        try:
            for i, v in enumerate(s): # Get index and value because we hope to return index but remove/add value
                s.pop(i) # Remove the value by index
                if v not in s: # Check if it still exists, if it does then it isn't unique
                    return i # Return the index if it doesn't already exist
                s.insert(i, v) # Put it back because it already existed

            return -1 # If the above loop never triggered then they must all be duplicates
        except:
            return -1 # if inputs empty or anything then it would return -1 anyway