class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [-1, -1, -1]
        output = 0

        for i, x in enumerate(s) :
            abc[ord(x) - ord('a')] = i
            if -1 not in abc :
                output += 1 + min(abc)

        return output