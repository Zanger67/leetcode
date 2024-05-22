# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return (1 + n) * n // 2 - ((m * (1 + n // m)) * (n // m))