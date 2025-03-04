class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n == 1 or \
               n > 0 and (bin(n)[2:][-2:].count('1') == 0) \
                     and (bin(n)[-3:1:-2].count('1') == 1) \
                     and (bin(n)[-4:1:-2].count('1') == 0)