class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        left, right = 0, len(nums) - 1

        for i in range(len(output) - 1, -1, -1) :
            if abs(nums[left]) > abs(nums[right]) :
                output[i] = nums[left] ** 2
                left += 1
            else :
                output[i] = nums[right] ** 2
                right -= 1

        return output