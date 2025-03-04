class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n >= 1 and (n == 1 or n // 3 * 3 == n and self.isPowerOfThree(n // 3))