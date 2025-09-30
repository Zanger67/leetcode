class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        output = 0
        for i, num in enumerate(nums) :
            output += num * comb(len(nums) - 1, i)

        return output % 10