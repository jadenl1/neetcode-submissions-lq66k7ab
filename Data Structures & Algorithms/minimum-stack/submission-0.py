class MinStack:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack2:
            self.stack2.append(val)
        else:
            lower = min(val, self.stack2[-1])
            self.stack2.append(lower)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.stack2:
            self.stack2.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        return -1