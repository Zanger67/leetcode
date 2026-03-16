class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.w_ranges = [0] * (len(w) + 1)
        for i in range(len(w)) :
            self.w_ranges[i + 1] = self.w_ranges[i] + w[i] / total
        

    def pickIndex(self) -> int:
        rand = random.random()
        indx = bisect.bisect(self.w_ranges, rand) - 1
        return indx

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()