class Solution: 
    def minFlips(self, grid: List[List[int]]) -> int:
        totalCount = 0

        # Parabolic both in rows and cols basically means
        # if you mirror a point to each quadrant,
        # then is it equal?
        #
        # If they are then it's already a multiple of 4.
        # If not, make the fewest changes.
        for cOffset in range(len(grid[0]) // 2) :
            for rOffset in range(len(grid) // 2) :
                ones = grid[rOffset][cOffset] \
                        + grid[len(grid) - rOffset - 1][cOffset] \
                        + grid[len(grid) - rOffset - 1][len(grid[0]) - cOffset - 1] \
                        + grid[rOffset][len(grid[0]) - cOffset - 1]
                totalCount += min(ones, 4 - ones)

        # Fixing the middle row if there is one (odd # of rows)
        changeMidRow = 0
        midRowOnes = 0
        flippedR = 0
        if len(grid) % 2 == 1 :
            indx = len(grid) // 2
            for i in range(len(grid[0]) // 2) :
                if grid[indx][i] != grid[indx][len(grid[0]) - i - 1] :
                    flippedR += 1
                    changeMidRow += 1
                else :
                    midRowOnes += grid[indx][i] * 2

        # Fixing the middle col if there is one (odd # of cols)
        changeMidCol = 0
        midColOnes = 0
        flippedC = 0
        if len(grid[0]) % 2 == 1 :
            indx = len(grid[0]) // 2
            for i in range(len(grid) // 2) :
                if grid[i][indx] != grid[len(grid) - i - 1][indx] :
                    changeMidCol += 1
                    flippedC += 1
                else :
                    midColOnes += grid[i][indx] * 2

        # Values that aren't matches MUST be fixed
        totalCount += changeMidCol + changeMidRow

        # If the totals don't add to a multiple of 4
        diff = ((midRowOnes + midColOnes) % 4)
        # Number of values matched via flipping
        totalEitherOr = (flippedC + flippedR) * 2

        # If diff is a multiple of 2 and we've flipped,
        # then we can just  "flip" one pair to 0
        #
        # If we haven't made flips before, we have an edge case
        if diff == 2 and totalEitherOr == 0 :
            totalCount += 2
        elif diff % 2 == 1:
            totalCount += min(diff, 4 - diff)

        # Middle middle (i.e. if odd # rows and cols), it MUST be
        # set to zero. If it's not, the total will be odd (not a x4).
        # Our previous checks go up to but don't include this point.
        if len(grid[0]) % 2 == 1 and len(grid) % 2 == 1 :
            totalCount += grid[len(grid) // 2][len(grid[0]) // 2]

        return totalCount
