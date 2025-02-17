class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        i1, i2 = 0, 0
        while i1 < len(s) and i2 < len(t) :
            if s[i1] == t[i2] :
                i1 += 1
                i2 += 1
                continue

            if i1 > i2 :
                return i2
            i1 += 1

        return i2