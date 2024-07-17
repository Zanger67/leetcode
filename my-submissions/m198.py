class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0] + nums.copy()

        for i in range(2, len(dp)) :
            dp[i] = max(dp[i] + dp[i - 2], dp[i - 1])

        return dp[-1]