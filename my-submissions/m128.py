# https://leetcode.com/problems/longest-consecutive-sequence/description/


# O(n) solution babyyyy

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        
        vals = set(nums)                # O(n) creation, O(1) lookups

        maxx = 0
        for val in vals:                # O(n) looping
            if val - 1 in vals:         # not start of sequence
                continue
            
            cnter = 1
            while val + cnter in vals :
                cnter += 1

            maxx = max(maxx, cnter)

        return maxx
