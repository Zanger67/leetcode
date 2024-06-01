# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/description/


# V2 is a bit faster fluctuating around the 75% mark


class Solution:
    def numSplits(self, s: str) -> int:
        counter = 0

        left, right = set(), set()
        lefty, righty = [0] * len(s), [0] * len(s)
        
        for i in range(0, len(s)) :
            left.add(s[i])
            right.add(s[len(s) - i - 1])
            
            lefty[i] = len(left)
            righty[len(s) - i - 1] = len(right)
        
        for i in range(len(s) - 1) :
            if lefty[i] == righty[i + 1] :
                counter += 1

        return counter
            

