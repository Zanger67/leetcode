class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return any(goal == s[i:] + s[:i] for i in range(len(s)))
