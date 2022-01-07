class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.Stack = []
    def push(self, x: int) -> None:
        if(len(self.Stack) < self.maxSize):
            self.Stack.append(x)
    def pop(self) -> int:
        if(self.Stack):
            return self.Stack.pop()
        return -1
    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if(i < len(self.Stack)):
                self.Stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
