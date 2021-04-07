class Solution:
    def romanToInt(self, s: str) -> int:
        array = []
        result = 0
        for k in s:
            array.append(k)


        for i in range(len(array)-1):
            # Uper Checks
            if array[i] == 'I' and array[i+1] == 'V':
                result = result + 4
            elif array[i] == 'I' and array[i+1] == 'X':
                result = result + 9
            # Single Check
            elif i == 0:
                if array[0] == 'I': result = result + 1
                if array[0] == 'V': result = result + 5
                if array[0] == 'X': result = result + 10
                if array[0] == 'L': result = result + 50
                if array[0] == 'C': result = result + 100
                if array[0] == 'D': result = result + 500
                if array[0] == 'M': result = result + 1000
            elif array[i] == 'I':
                result = result + 1
            # Lower Checks
            elif i != 0:
                if array[i] == 'V' and array[i-1] != 'I':
                    result = result + 5
                elif array[i] == 'X' and array[i-1] != 'I':
                    result = result + 10
        # Don't forget to add the last roman numeral missed in the above loop
        return result

sol = Solution()

print(sol.romanToInt('IXIVe'))