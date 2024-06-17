class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0


        def fillOutIsland(row: int, col: int) :
            if 0 <= row < len(grid) \
                and 0 <= col < len(grid[0]) \
                and grid[row][col] == '1' :
                grid[row][col] = '0'
                fillOutIsland(row - 1, col)
                fillOutIsland(row + 1, col)
                fillOutIsland(row, col - 1)
                fillOutIsland(row, col + 1)
            
        for row in range(len(grid)) :
            for col in range(len(grid[0])) :
                if grid[row][col] == '1' :
                    counter += 1
                    fillOutIsland(row, col)

        return counter