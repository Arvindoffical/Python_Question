class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = [0] * maxSize
    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc[len(self.stack) - 1] = 0
    def pop(self) -> int:
        if not self.stack:
            return -1
        idx = len(self.stack) - 1
        res = self.stack[idx] + self.inc[idx]
        self.stack.pop()
        if idx > 0:
            self.inc[idx - 1] += self.inc[idx]
        return res
    def increment(self, k: int, val: int) -> None:
        if self.stack:
            idx = min(k, len(self.stack)) - 1
            self.inc[idx] += val
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)