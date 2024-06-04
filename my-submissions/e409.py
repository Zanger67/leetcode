# https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        return sum([(x // 2) * 2 for x in cnt.values()]) + (1 if sum([x % 2 for x in cnt.values()]) > 0 else 0)