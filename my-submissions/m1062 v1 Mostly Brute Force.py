class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        longest = 0
        substr = set()
        for i in range(len(s)) :
            for j in range(i + 1 + longest, len(s) + 1) :
                if s[i:j] in substr :
                    longest = j - i
                else :
                    substr.add(s[i:j])

        return longest