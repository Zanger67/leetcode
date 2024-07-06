class CustomStack:

    def __init__(self, maxSize: int):
        self.stk = []
        self.maxx = maxSize

    def push(self, x: int) -> None:
        if len(self.stk) >= self.maxx :
            return
        self.stk.append(x)

    def pop(self) -> int:
        if not self.stk :
            return -1
        return self.stk.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stk))) :
            self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)