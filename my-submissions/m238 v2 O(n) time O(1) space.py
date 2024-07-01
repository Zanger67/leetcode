# Question restriction: Must be O(n) and CANNOT use division
# FOLLOWUP RESTRICTION: O(1) space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time and O(n) space
        output = [1] * len(nums)
        output[1] = nums[0]

        # O(n) time O(1) space
        for i in range(2, len(nums)) :
            output[i] = output[i - 1] * nums[i - 1]

        # O(n) time
        for i in range(len(nums) - 2, -1, -1) :
            output[i] *= nums[i + 1]
            nums[i] *= nums[i + 1]

        return output