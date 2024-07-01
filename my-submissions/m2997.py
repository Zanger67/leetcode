class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xored = k
        for num in nums :
            xored ^= num

        count = 0
        while xored > 0 :
            if xored % 2 == 1 :
                count += 1
            
            xored = xored >> 1
        return count