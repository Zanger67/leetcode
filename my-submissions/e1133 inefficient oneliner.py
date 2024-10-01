# Slow but funny oneliner
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        return max(nums + [-1], key=lambda x: (-Counter(nums + [-1])[x], x))
