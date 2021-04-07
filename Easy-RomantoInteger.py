class Solution:
    def romanToInt(self, s: str) -> int:
        array = []
        result = 0
        for k in s:
            array.append(k)
        for i in range(len(array)-1):
            """Looking for I, IV and IX"""
            if array[i] == 'I' and array[i+1] == 'V':
                result = result + 4
            elif array[i] == 'I' and array[i+1] == 'X':
                result = result + 9
            elif array[i] == 'I':
                result = result + 1
            elif i == 0 and array[i] == 'V':
                result = result + 5
            elif i != 0:
                if array[i] == 'V' and array[i-1] != 'I':
                    result = result + 5
        # Don't forget to add the last roman numeral missed in the above loop
        return result

sol = Solution()

print(sol.romanToInt('V'))