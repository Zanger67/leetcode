#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n > 0 :
            if n % 2 == 1 :
                counter += 1
            n //= 2
        return counter
# @lc code=end

