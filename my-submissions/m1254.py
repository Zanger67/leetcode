class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def deleteIsland(row: int, col: int) -> None :
            if not (0 <= row < len(grid)) or not (0 <= col < len(grid[0])) :
                return
            if grid[row][col] :
                return
            
            grid[row][col] = 1

            deleteIsland(row + 1, col)
            deleteIsland(row - 1, col)
            deleteIsland(row, col + 1)
            deleteIsland(row, col - 1)

        for i in range(len(grid)) :
            if not grid[i][0] :
                deleteIsland(i, 0)
            if not grid[i][len(grid[0]) - 1] :
                deleteIsland(i, len(grid[0]) - 1)

        for i in range(1, len(grid[0]) - 1) :
            if not grid[0][i] :
                deleteIsland(0, i)
            if not grid[len(grid) - 1][i] :
                deleteIsland(len(grid) - 1, i)

        counter = 0

        for row in range(len(grid)) :
            for col in range(len(grid[0])) :
                if not grid[row][col] :
                    counter += 1
                    deleteIsland(row, col)
        
        return counter