class Solution:
    def fizzBuzz(self, n: int):
        result = []
        count = 1
        while count <= n:
            if count % 15 == 0:
                result.append('FizzBuzz')
            elif count % 5 == 0:
                result.append('Buzz')
            elif count % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(count))
            count += 1
        return result

sol = Solution()
print(sol.fizzBuzz(100))