class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        
        return self.triangularSum([(x + y) % 10 for x, y in zip(nums[:-1], nums[1:])])
