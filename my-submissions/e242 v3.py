# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (len(s) == len(t)) and (Counter(s) == Counter(t))