class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums) - 2) :
            if nums[i] + nums[i + 2] == nums[i + 1] / 2 :
                output += 1
        return output