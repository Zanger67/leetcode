# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/description/

# Did during Weekly Contest 400

class Solution:
    def minimumChairs(self, s: str) -> int:
        maxx = 0
        curr = 0
        for i in s :
            if i == 'L' :
                curr = max(0, curr - 1)
            else :
                curr += 1
                maxx = max(curr, maxx)
        return maxx