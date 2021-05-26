class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []
        

    def push(self, val: int) -> None:
        self.array.append(val)
        

    def pop(self) -> None:
        self.array.pop(-1)
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        result = self.array[0]
        for i in self.array:
            if i < result:
                result = i
        return result