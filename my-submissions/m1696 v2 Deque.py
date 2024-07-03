class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 :
            return nums[0]

        dp = deque()
        dp.append((nums[0], 0))

        for i in range(1, len(nums)) :
            while dp[-1][1] < i - k :
                dp.pop()
            val = dp[-1][0] + nums[i]

            while dp and (dp[0][0] <= val or dp[0][1] < i - k + 1) :
                dp.popleft()
            dp.appendleft((val, i))

        return dp[0][0]