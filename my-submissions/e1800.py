class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = []
        summ = 0
        maxx = 0
        for num in nums :
            if curr and curr[-1] >= num :
                maxx = max(maxx, summ)
                summ = 0
                curr = []
            curr.append(num)
            summ += num
        return max(maxx, summ)
