# firmly in the 50% region with little variance
# From the right side using deque to skip characters


class Solution:
    def removeStars(self, s: str) -> str:
        starCounter = 0
        rightSide = deque()
        for i in reversed(s) :
            if i == '*':
                starCounter += 1
                continue
            
            if starCounter == 0 :
                rightSide.appendleft(i)
                continue
            
            starCounter -= 1

        return ''.join(list(rightSide))