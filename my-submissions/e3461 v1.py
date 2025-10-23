class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2 :
            s_n = []
            for x, y in zip(s[:-1], s[1:]) :
                s_n.append(str((int(x) + int(y)) % 10))
            s = ''.join(s_n)
        
        return s[0] == s[1]