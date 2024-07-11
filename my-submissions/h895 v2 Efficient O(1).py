class FreqStack:

    def __init__(self):
        self.val_freqs = defaultdict(int)
        self.freq_vals = defaultdict(list)
        self.maxx = 0

    def push(self, val: int) -> None:
        self.val_freqs[val] += 1
        self.maxx = max(self.maxx, self.val_freqs[val])
        self.freq_vals[self.val_freqs[val]].append(val)

    def pop(self) -> int:
        if not self.freq_vals[self.maxx] :
            self.maxx -= 1
        
        out = self.freq_vals[self.maxx].pop()
        self.val_freqs[out] -= 1
        return out


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()