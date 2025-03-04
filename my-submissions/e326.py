class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and n == 3 ** int(log(n, 3) + 0.0001)