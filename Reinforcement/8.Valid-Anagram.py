class Solution:
    def isAnagram(self, s, t):
        """ "anagram" & "nagaram" """
        try: # Since the result is only true or false it's worth adding an exception to catch wild edge cases
            sSort = sorted(s) # ['a', 'a', 'a', 'g', 'm', 'n', 'r']
            tSort = sorted(t) # ['a', 'a', 'a', 'g', 'm', 'n', 'r']

            return sSort == tSort # Since above match, True is returned. Better than using an if/else
            
        except:
            return False # False because if the above fails it's likely the inputs would've equated false anyway