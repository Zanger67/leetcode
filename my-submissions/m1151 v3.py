class Solution:
    def minSwaps(self, data: List[int]) -> int:
        data = [0] + list(accumulate(data))
        tot_ones = data[-1]
        return tot_ones - max(data[i + tot_ones] - data[i] for i in range(len(data) - tot_ones))