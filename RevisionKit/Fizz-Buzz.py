class Solution:
    def fizzBuzz(self, n):
        """ 3 """
        result = [] # Prepare an array for the results
        
        for i in range(1, n + 1): # We don't want zero and we want the last number in the range
            if i % 15 == 0: # Searching fizzbuzz first prevents getting fizz buzz or just buzz, note it's an elif
                result.append('FizzBuzz')
            elif i % 5 == 0: # Modulo finds the remainder, if nothing it's a multiple of 15/5/3
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i)) # The output equires each element in the array to be a string
        
        return result