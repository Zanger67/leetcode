# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2 :
            return [0, 1]

        differences = {}
        for i in range(len(nums)) :
            if nums[i] in differences.keys() :
                return [i, differences.get(nums[i])]
            differences[target - nums[i]] = i
        return [0, 0]
        