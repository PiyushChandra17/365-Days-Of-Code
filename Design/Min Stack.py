class MinStack:

    def __init__(self):
        self.stack = []
        
        

    def push(self, x: int) -> None:
        self.stack.append((x,min(self.getMin(),x)))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize