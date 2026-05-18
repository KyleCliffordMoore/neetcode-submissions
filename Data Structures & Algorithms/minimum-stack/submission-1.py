class MinStack:

    def __init__(self):
        self.decrstack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.decrstack) > 0:
            if val <= self.decrstack[-1]:
                self.decrstack.append(val)
        else:
            self.decrstack.append(val)
            
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.decrstack[-1]:
            self.decrstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.decrstack[-1]