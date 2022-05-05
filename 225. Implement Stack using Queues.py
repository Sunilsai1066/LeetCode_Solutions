class MyStack:
    def __init__(self):
        self.Queue = []

    def push(self, x: int) -> None:
        self.Queue.append(x)
        for i in range(len(self.Queue)-1):
            self.Queue.append(self.Queue.pop(0))

    def pop(self) -> int:
        return self.Queue.pop(0)

    def top(self) -> int:
        return self.Queue[0]

    def empty(self) -> bool:
        return self.Queue == []


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
