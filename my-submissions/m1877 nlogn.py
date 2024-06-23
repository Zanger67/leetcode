class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxx = 0

        for i in range(len(nums) // 2) :
            maxx = max(maxx, nums[i] + nums[len(nums) - i - 1])

        return maxx