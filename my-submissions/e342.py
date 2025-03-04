class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n >= 1 and (n == 1 or n // 4 * 4 == n and self.isPowerOfFour(n // 4))