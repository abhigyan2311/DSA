# Using 2 stacks - O(N), O(2N)
# class MyQueue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def push(self, x: int) -> None:
#         while self.s1:
#             self.s2.append(self.s1.pop())
#         self.s1.append(x)
#         while self.s2:
#             self.s1.append(self.s2.pop())

#     def pop(self) -> int:
#         return self.s1.pop()

#     def peek(self) -> int:
#         return self.s1[-1]

#     def empty(self) -> bool:
#         return len(self.s1) == 0

# Using 2 stacks
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        if self.output:
            return self.output.pop()
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output.pop()

    def peek(self) -> int:
        if self.output:
            return self.output[-1]
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == 0 and len(self.output) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()