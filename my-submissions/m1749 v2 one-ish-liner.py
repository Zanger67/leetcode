class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # kadane's but for both min and max
        output = abs(nums[0])
        minn, maxx = nums[0], nums[0]

        return max([(output := max(output, (maxx := max(maxx + num, num)), -(minn := min(minn + num, num)))) for num in nums[1:]] + [output])