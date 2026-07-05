class MinStack:

    def __init__(self):
        self.test = []

    def push(self, val: int) -> None:
        self.test.append(val)

    def pop(self) -> None:
        self.popValue = self.test.pop()
        
    def top(self) -> int:
        return self.test[-1]

    def getMin(self) -> int:
        return min(self.test)
