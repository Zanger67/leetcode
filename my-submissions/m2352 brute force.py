class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        horizontal = {}
        vertical = {}

        for i, row in enumerate(grid) :
            horizontal[i] = tuple(row)
        
        for j in range(len(grid[0])) :
            vertical[j] = tuple([grid[i][j] for i in range(len(grid))])
        
        output = 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if horizontal[i] == vertical[j] :
                    output += 1

        return output