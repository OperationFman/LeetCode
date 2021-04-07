class Solution:
    def romanToInt(self, s: str) -> int:
        array = []
        result = 0
        for k in s:
            array.append(k)

        if array[0] == 'I': result = result + 1
        if array[0] == 'V': result = result + 5
        if array[0] == 'X': result = result + 10
        if array[0] == 'L': result = result + 50
        if array[0] == 'C': result = result + 100
        if array[0] == 'D': result = result + 500
        if array[0] == 'M': result = result + 1000

        for i in range(len(array)-1):
            if i == 0:
                continue
            elif array[i] == 'I' and array[i+1] == 'V':
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

print(sol.romanToInt('IIe'))