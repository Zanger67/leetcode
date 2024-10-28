class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        vals = set(nums)
        nums.sort(reverse=False)
        max_streak = 0

        for num in nums :
            cnt = 1
            curr = num ** 2
            while vals and curr in vals :
                vals.remove(curr)           # optimizing
                cnt += 1
                curr = curr ** 2
            max_streak = max(max_streak, cnt)

        return max_streak if max_streak > 1 else -1
