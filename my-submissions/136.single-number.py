#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xored = 0
        for num in nums :
            xored ^= num
        return xored
# @lc code=end

