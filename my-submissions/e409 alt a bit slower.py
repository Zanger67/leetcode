# https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04


class Solution:
    def longestPalindrome(self, s: str) -> int:
        refSet = set()

        count = 0
        for c in s :
            if c in refSet :
                refSet.remove(c)
                count += 2
            else :
                refSet.add(c)

        return count + (1 if len(refSet) > 0 else 0)