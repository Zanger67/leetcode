# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        current = 0

        while current * current <= x :
            current += 1
        return current - 1