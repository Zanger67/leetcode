class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros, right_ones = 0, s.count('1')
        maxx = 0

        for c in s[:-1] :
            if c == '0' :
                left_zeros += 1
            else :
                right_ones -= 1
            maxx = max(maxx, left_zeros + right_ones)
        
        return maxx
