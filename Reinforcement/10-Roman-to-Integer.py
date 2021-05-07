class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        array = { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = array[s[0]
        for _, i in enumerate(s):
            if array[i] > count:
                result = result + array[i]
                result = result - count * 2
                count = array[i]
            else:
                result += array[i]
                count = array[i]
        return result