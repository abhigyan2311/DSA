class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append((val, val))
        else:
            topEL = self.st[-1]         
            if val < topEL[1]:
                self.st.append((val, val))
            else:
                self.st.append((val, topEL[1]))

    def pop(self) -> None:
        if self.st: self.st.pop()

    def top(self) -> int:
        if self.st: return self.st[-1][0]

    def getMin(self) -> int:
        if self.st: return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
