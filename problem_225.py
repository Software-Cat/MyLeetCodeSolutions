from collections import deque


class MyStack:
    def __init__(self):
        self.q: deque[int] = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        ret = self.q.pop()
        self.q.append(ret)
        return ret

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

myStack = MyStack()
myStack.push(1)
myStack.push(2)
myStack.top()  # return 2
myStack.pop()  # return 2
myStack.empty()  # return False
