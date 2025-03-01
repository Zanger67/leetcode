class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # convert data into a prefix sum starting at zero
        running_total = 0
        for i in range(len(data)) :
            data[i], running_total = running_total, running_total + data[i]
        data.append(running_total)

        tot_ones = data[-1]

        # Find window of size tot_ones with the most ones already there
        output = 0
        for i in range(tot_ones, len(data)) :
            output = max(output, data[i] - data[i - tot_ones])

        return tot_ones - output