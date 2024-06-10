# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s.replace(' ', '')) == 0 :
            return 0
        positive = True
        leftIndx = 0

        while s[leftIndx] == ' ' :
            leftIndx += 1

        if s[leftIndx] == '-' :
            positive = False
            leftIndx += 1
        elif s[leftIndx] == '+' :
            leftIndx += 1

        rightIndx = leftIndx
        while rightIndx < len(s) and s[rightIndx].isnumeric() :
            rightIndx += 1
        
        if (leftIndx == rightIndx) :
            return 0
        
        output = int(s[leftIndx:rightIndx]) * (1 if positive else -1)
        return min(max(output, -1 * (2**31)), 2**31 - 1)
        