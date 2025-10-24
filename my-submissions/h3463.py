class Solution:
    def hasSameDigits(self, s: str) -> bool:
        x = len(s) - 2
        a = sum((int(num) * comb(x, i)) % 10 for i, num in enumerate(s[:-1])) % 10
        b = sum((int(num) * comb(x, i)) % 10 for i, num in enumerate(s[1:])) % 10
        return a == b