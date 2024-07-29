class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = [grid[0]] + [[inf] * len(grid[0]) for _ in range(len(grid) - 1)]

        # Iterating through the rows from 0 to the one prior to last
        for r in range(len(dp) - 1) :
            # Iterating each column
            # (r, c) = grid source indx
            for c in range(len(dp[0])) :
                # Iterating through the potential future spots
                for nxtCol in range(len(dp[0])) :
                    # Calculating the new value and setting it if it's cheaper
                    nxtVal = dp[r][c] + moveCost[grid[r][c]][nxtCol] + grid[r + 1][nxtCol]
                    
                    if dp[r + 1][nxtCol] > nxtVal :
                        dp[r + 1][nxtCol] = nxtVal

        return min(dp[-1])