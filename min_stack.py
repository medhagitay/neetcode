class MinStack:

    def __init__(self):
        self.stack=[]
        self.tp=-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.tp+=1

    def pop(self) -> None:
        self.stack.pop()
        self.tp-=1

    def top(self) -> int:
        return self.stack[self.tp]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()