# https://leetcode.com/problems/strictly-palindromic-number/

# Intuition: none will be cause for any value n, n in the 
# base n-2 will be something 100000...000 as the (n-2) value,
# plus 00000..0002 for the other end cause of the offset.

class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False