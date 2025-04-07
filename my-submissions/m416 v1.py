class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 :
            return False
        dp = [True] + [False] * (tot // 2)

        for num in nums :
            for i in range(len(dp) - 1, num - 1, -1) :
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]
