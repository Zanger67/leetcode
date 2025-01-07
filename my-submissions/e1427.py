class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        x = (sum([-x[1] if x[0] else x[1] for x in shift]) + len(s)) % len(s)
        return s[x:] + s[:x]
