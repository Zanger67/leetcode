# https://leetcode.com/problems/score-of-a-string/description/?envType=daily-question&envId=2024-06-01

class Solution:
    def scoreOfString(self, s: str) -> int:
        output = 0

        for i in range(0, len(s) - 1) :
            output += abs(ord(s[i]) - ord(s[i + 1]))
        
        return output