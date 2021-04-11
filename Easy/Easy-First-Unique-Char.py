class Solution:
    def firstUniqChar(self, s: str) -> int:
        array = list(s)
        for i in array:
            index = array.index(i)
            array.pop(index)
            if i not in array:
                return index
            array.insert(index, i)
        return -1

sol = Solution()
print(sol.firstUniqChar('hellothere')) # o (index 4) is the first non-repeated character
print(sol.firstUniqChar('aabbccdd')) # All characters are repeated, returns -1