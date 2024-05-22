# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self.climbStairsBottomUp(0, n)

    @cache
    def climbStairsBottomUp(self, curr: int, n: int) -> int:
        if (curr == n) :
            return 1
        if (curr > n) :
            return 0
        return self.climbStairsBottomUp(curr + 1, n) + self.climbStairsBottomUp(curr + 2, n)