class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0

        vals = set(nums)                # O(n) creation, O(1) lookups

        maxx = 0
        while vals :
            left = right = vals.pop()
            curr = 1
            while left - 1 in vals :
                left -= 1
                curr += 1
                vals.remove(left)
            while right + 1 in vals :
                right += 1
                curr += 1
                vals.remove(right)

            maxx = max(maxx, curr)

        return maxx
