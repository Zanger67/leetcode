class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max((pos := sum(x > 0 for x in nums)), len(nums) - nums.count(0) - pos)