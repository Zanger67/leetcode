class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums) 

        for i in range(1, len(nums)) :
            nums[i] += nums[i - 1]
        
        return [bisect_right(nums, i) for i in queries]