# Redo this at a later date

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        val     = 0
        indx    = 0

        while val < n :
            if indx < len(nums) and nums[indx] <= val + 1 :
                val  += nums[indx]
                indx += 1
            else :
                val     = 2 * val + 1
                patches += 1

        return patches

