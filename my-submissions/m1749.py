class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # kadane's but for both min and max
        output = abs(nums[0])

        max_sub_arr = nums[0]
        min_sub_arr = nums[0]

        for num in nums[1:] :
            max_sub_arr = max(max_sub_arr + num, num)
            min_sub_arr = min(min_sub_arr + num, num)
            output = max(output, max_sub_arr, -min_sub_arr)

        return output
