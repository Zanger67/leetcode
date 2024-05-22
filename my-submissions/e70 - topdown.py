# https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    record = {}
    def climbStairs(self, n: int) -> int:
        if (n == 0 or n == 1) :
            return 1
        if (n not in self.record) :
            self.record[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.record[n]
