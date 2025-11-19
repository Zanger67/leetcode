class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        output = 0
        while original in nums :
            output += 1
            original *= 2
        return original