# Redo this at a later date


''' Notes

    If your target is [1, n] and you have [1, 6], then you can 
    keep adding the next smallest value, extending your reach by 2x

    The result is n - 6 = 2 ^ ? where ? is what you need to add,

'''


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

