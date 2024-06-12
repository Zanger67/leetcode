# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xored = k
        for num in nums :
            xored ^= num

        return xored.bit_count()