class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    @cache
    def findIndx(self, value: int) -> (int, int) :
        for r in range(len(self.grid)) :
            for c in range(len(self.grid[0])) :
                if self.grid[r][c] == value :
                    return r, c
        return -1, -1

    @cache
    def adjacentSum(self, value: int) -> int:
        r, c = self.findIndx(value)

        output = 0
        if r - 1 >= 0 :
            output += self.grid[r - 1][c]
        if r + 1 < len(self.grid) :
            output += self.grid[r + 1][c]
        if c + 1 < len(self.grid[0]) :
            output += self.grid[r][c + 1]
        if c - 1 >= 0 :
            output += self.grid[r][c - 1]
        return output

    @cache
    def diagonalSum(self, value: int) -> int:
        r, c = self.findIndx(value)

        output = 0
        if r - 1 >= 0 and c - 1 >= 0 :
            output += self.grid[r - 1][c - 1]
        if r - 1 >= 0 and c + 1 < len(self.grid[0])  :
            output += self.grid[r - 1][c + 1]
        if r + 1 < len(self.grid) and c - 1 >= 0 :
            output += self.grid[r + 1][c - 1]
        if r + 1 < len(self.grid) and c + 1 < len(self.grid[0]):
            output += self.grid[r + 1][c + 1]
        return output
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)