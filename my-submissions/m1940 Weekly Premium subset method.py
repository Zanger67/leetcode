# https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/description/?envType=weekly-question&envId=2024-06-01
# weekly premium question

# Rank: 1

# Notably faster than the iterative approach, perhaps due to the O(1) set usage?
# I think this is O(n*m) where n is the total number of terms in all arrays summed
# and m is the max number of terms in a single subarray
# --> cost is due to the intersection being O(m) max case and done n-1 times

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        outputSet = set(arrays[0])

        for arrayCase in arrays :
            outputSet &= set(arrayCase)

        return sorted(list(outputSet))
