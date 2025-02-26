class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        max_sum = nums[0]
        for num in nums[1:] :
            max_sum = max(max_sum + num, num)
            output = max(max_sum, output)
        return output