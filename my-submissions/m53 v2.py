class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = -inf
        max_sum = -inf
        for num in nums :
            max_sum = max(max_sum + num, num)
            output = max(max_sum, output)
        return output