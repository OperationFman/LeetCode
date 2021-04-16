class Solution:
    def isValid(self, s: str) -> bool:
        try:
            string = s
            stack = []
            openBrackets = ['(', '{', '[', '<']
            closeBrackets = [')', '}', ']', '>']
            for i in string:
                if i in openBrackets:
                    stack.append(i)
                if i in closeBrackets:
                    c = closeBrackets.index(i) #get the index of the close which matches the open
                    if openBrackets[c] not in stack:
                        return False
                    if openBrackets[c] == stack[-1]:
                        stack.pop()
            if stack == []:
                return True
            else:
                return False
        except:
            return False

sol = Solution()

print(sol.isValid('<()>'))
print(sol.isValid('(])'))