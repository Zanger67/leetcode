class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        return sum(x % 2 for x in Counter(s).values()) <= 1