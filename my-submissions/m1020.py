class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def removeNonEnclave(row: int, col: int) -> None :
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) :
                return
            if not grid[row][col] :
                return
            
            grid[row][col] = 0

            removeNonEnclave(row + 1, col)
            removeNonEnclave(row - 1, col)
            removeNonEnclave(row, col + 1)
            removeNonEnclave(row, col - 1)

        for i in range(len(grid)) :
            if grid[i][0] :
                removeNonEnclave(i, 0)
            if grid[i][len(grid[0]) - 1] :
                removeNonEnclave(i, len(grid[0]) - 1)

        for i in range(1, len(grid[0]) - 1) :
            if grid[0][i] :
                removeNonEnclave(0, i)
            if grid[len(grid) - 1][i] :
                removeNonEnclave(len(grid) - 1, i)
        

        counter = 0
        for row in range(1, len(grid)) :
            for col in range(len(grid[0])) :
                if grid[row][col] :
                    counter += 1
        
        return counter