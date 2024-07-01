class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xored = k
        for num in nums :
            xored ^= num

        return xored.bit_count()