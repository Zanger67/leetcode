class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowCounts = [0] * len(grid)
        colCounts = [0] * len(grid[0])

        for i in range(len(grid)) :
            rowCounts[i] = sum(grid[i])

        for i in range(len(grid[0])) :
            for j in range(len(grid)) :
                colCounts[i] += grid[j][i]
        
        output = []
        for i in range(len(grid)) :
            output.append([])

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                output[i].append(2 * (colCounts[j] + rowCounts[i]) - len(grid) - len(grid[0]))
        return output