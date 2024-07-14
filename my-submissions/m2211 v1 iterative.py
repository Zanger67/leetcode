class Solution:
    def countCollisions(self, directions: str) -> int:
        cols = 0
        lCounter = 0
        last = 'R'

        for c in reversed(directions) :
            if c == 'L' :
                lCounter += 1
                last = c

            elif c == 'S' :
                cols += lCounter
                lCounter = 0
                last = c

            elif c == 'R' and last != 'R' : # R
                cols += lCounter + 1
                lCounter = 0
                last = 'S'

        return cols
