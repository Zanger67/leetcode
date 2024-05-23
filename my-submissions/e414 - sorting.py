# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        newNums = sorted(list(set(nums)))
        return newNums[len(newNums) - (3 if len(newNums) >= 3 else 1)]