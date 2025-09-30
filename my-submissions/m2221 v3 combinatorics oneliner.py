class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        return sum(num * comb(len(nums) - 1, i) for i, num in enumerate(nums)) % 10
