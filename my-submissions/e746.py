class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * 2 + [0] * len(cost)
        for i, cost in enumerate(cost, 2) :
            dp[i] = cost + min(dp[i - 1], dp[i - 2])
        return min(dp[-2:])