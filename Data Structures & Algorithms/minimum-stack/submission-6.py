class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix:
            # TODO: nothing below, so what's the prefix min?
            self.prefix.append(val)
        else:
            # TODO: append the smaller of val and the current prefix min
            if val < self.prefix[-1]:
                self.prefix.append(val)
            else:
                self.prefix.append(self.prefix[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
