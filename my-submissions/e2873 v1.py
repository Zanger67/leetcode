class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        return max([
            (u - v) * w for i, u in enumerate(nums[:-2]) 
            for j, v in enumerate(nums[i + 1:-1], i + 1)
            for k, w in enumerate(nums[j + 1:], j + 1)] + [0]
        )