# https://leetcode.com/problems/guess-the-number-using-bitwise-questions-i/

# Definition of commonSetBits API.
# def commonSetBits(num: int) -> int:

class Solution:
    def findNumber(self) -> int:
        output = 0
        current = 1
        for i in range(31) :
            if commonSetBits(current) :
                output += current
            current *= 2
        return output