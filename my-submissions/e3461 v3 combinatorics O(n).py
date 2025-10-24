class Solution:
    def hasSameDigits(self, s: str) -> bool:
        a, b = 0, 0
        x = len(s) - 2
        for i, num in enumerate(s[:-1]) :
            a += (int(num) * comb(x, i)) % 10
        for i, num in enumerate(s[1:]) :
            b += (int(num) * comb(x, i)) % 10
        return a % 10 == b % 10