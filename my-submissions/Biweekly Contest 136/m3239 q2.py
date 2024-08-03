class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rowFlips = 0
        for r in range(len(grid)) :
            for i in range(len(grid[0]) // 2) :
                if grid[r][i] != grid[r][len(grid[0]) - i - 1] :
                    rowFlips += 1

        colFlips = 0
        for c in range(len(grid[0])) :
            for i in range(len(grid) // 2) :
                if grid[i][c] != grid[len(grid) - i - 1][c] :
                    colFlips += 1


        return min(colFlips, rowFlips)
