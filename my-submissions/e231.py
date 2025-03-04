class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n >= 1 and (n == 1 or n // 2 * 2 == n and self.isPowerOfTwo(n // 2))