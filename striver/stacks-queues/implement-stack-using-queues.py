from collections import deque

# Using 2 Queues
# class MyStack:
#     def __init__(self):
#         self.q1 = deque()
#         self.q2 = deque()

#     def push(self, x: int) -> None:
#         self.q2.append(x)
#         while len(self.q1) > 0:
#             self.q2.append(self.q1.popleft())
#         self.q1, self.q2 = self.q2, self.q1

#     def pop(self) -> int:
#         return self.q1.popleft()

#     def top(self) -> int:
#         if len(self.q1) > 0:
#             return self.q1[0]
#         else: return -1

#     def empty(self) -> bool:
#         return len(self.q1) == 0

# Using 1 Queue
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        n = len(self.q) - 1
        for _ in range(n):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        if len(self.q) > 0:
            return self.q[0]
        else: return -1

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
print(obj.pop())
print(obj.empty())