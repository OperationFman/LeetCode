class Solution:
    def isAnagram(self, s, t):
        try:
            sSort = sorted(list(s)) # Make string a list and sort it 
            tSort = sorted(list(t))

            if sSort == tSort: # If they dont match they arnt anagrams
                return True
            return False
        except:
            return False
