class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        return max((max_sum := max(max_sum + num, num)) for num in nums)