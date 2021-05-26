class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = [] # Need a data structure, array is the simplest but not the best, nor is it a stack
        

    def push(self, val: int) -> None:
        self.array.append(val) # Adds value onto the end of the stack. O(1)
        

    def pop(self) -> None:
        self.array.pop(-1) # array[-1] is O(1) since nothing before it needs replacing
        

    def top(self) -> int:
        return self.array[-1] # Also O(1)
        

    def getMin(self) -> int:
        result = self.array[0] # Set value to the first in the list, everything after that should be able to change it or it stays as is
        for i in self.array: # O(n)
            if i < result:
                result = i # Change the result if it's lower
        return result