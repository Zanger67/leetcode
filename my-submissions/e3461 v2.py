class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2 :
            s = ''.join([str((int(x) + int(y)) % 10) for x, y in zip(s[:-1], s[1:])])
        return s[0] == s[1]