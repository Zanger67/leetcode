# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        return sum([2 << x for x in range(0, 31) if commonSetBits(2 << x)]) + commonSetBits(1)