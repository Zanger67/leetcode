class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = [0, 0] + [0] * (len(nums))

        for i in range(0, len(nums)) :
            val1 = dp[i + 1] + nums[i]
            if i == 0 :
                val1 = nums[i]

            val2 = dp[i] + nums[i - 1] - nums[i]
            if i == 0 :
                val2 = -inf
            elif i == 1 :
                val2 = nums[i - 1] - nums[i]
            dp[i + 2] = max(val1, val2)

        return dp[-1]