class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([None for x in nums if (len(str(x)) + 1) % 2])