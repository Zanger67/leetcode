class FreqStack:

    def __init__(self):
        self.dt = {}
        self.cnter = 0

    def push(self, val: int) -> None:
        if val not in self.dt :
            self.dt[val] = [1, [self.cnter]]
        else :
            self.dt[val][0] += 1
            self.dt[val][1].append(self.cnter)
        self.cnter += 1

    def pop(self) -> int:
        out, freq, indx = -1, -1, -1

        for k, v in self.dt.items() :
            if v[0] > freq or (v[0] == freq and v[1][-1] > indx):
                freq = v[0]
                indx = v[1][-1]
                out = k

        self.dt[out][0] -= 1
        self.dt[out][1].pop()

        if self.dt[out][0] == 0 :
            self.dt.pop(out)

        return out


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()