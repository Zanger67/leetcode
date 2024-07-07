class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        for r in grid :
            print(r)

        rowMin, rowMax = inf, -inf
        colMin, colMax = inf, -inf

        found = False

        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] :
                    # print(f'{r, c = }')
                    found = True
                    if r < rowMin :
                        rowMin = r
                    if r > rowMax :
                        rowMax = r
                    
                    if c < colMin :
                        colMin = c
                    if c > colMax :
                        colMax = c

        if not found :
            return 0
            
        return max((colMax - colMin + 1), 1) * max((rowMax - rowMin + 1), 1)