class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # convert data into a prefix sum starting at zero
        running_total = 0
        for i in range(len(data)) :
            data[i], running_total = running_total, running_total + data[i]
        data.append(running_total)

        tot_ones = data[-1]

        return min(tot_ones - (data[i] - data[i - tot_ones]) for i in range(tot_ones, len(data)))