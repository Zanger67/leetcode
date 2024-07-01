class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)) :
            if grid[i][0] == 0 :
                self.flipRow(grid, i)
        
        for col in range(1, len(grid[0])) :
            colVal = sum(grid[x][col] for x in range(len(grid)))
            if colVal < len(grid) / 2 :
                self.flipCol(grid, col)
        
        # convert from binary
        runningSum = 0

        for row in grid :
            runningSum += int(''.join([str(x) for x in row]), 2)

        return runningSum


    def flipRow(self, grid: List[List[int]], x: int) -> None :
        ref = {0: 1, 1: 0}
        for i in range(len(grid[0])) :
            grid[x][i] = ref[grid[x][i]]

    def flipCol(self, grid: List[List[int]], x: int) -> None :
        ref = {0: 1, 1: 0}
        for i in range(len(grid)) :
            grid[i][x] = ref[grid[i][x]]