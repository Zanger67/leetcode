class Solution:
    def check(self, nums: List[int]) -> bool:
        allowance_used = False
        for i, j in zip(nums[:-1], nums[1:]) :
            if i <= j :
                continue
            if allowance_used :
                return False
            allowance_used = True
        return not allowance_used or (nums[0] >= nums[-1])