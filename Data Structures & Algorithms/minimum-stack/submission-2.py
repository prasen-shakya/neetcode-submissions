class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_vals = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        val = min(val, self.minimum_vals[-1] if self.minimum_vals else val)

        self.minimum_vals.append(val)
            



    def pop(self) -> None:
        self.stack.pop()
        self.minimum_vals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_vals[-1]
