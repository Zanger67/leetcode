class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        xes = [[0] * len(grid[0]) for _ in range(len(grid))]
        yes = [[0] * len(grid[0]) for _ in range(len(grid))]

        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if r > 0 :
                    xes[r][c] += xes[r - 1][c]
                    yes[r][c] += yes[r - 1][c]
                if c > 0 :
                    xes[r][c] += xes[r][c - 1]
                    yes[r][c] += yes[r][c - 1]
                if r > 0 and c > 0 :
                    xes[r][c] -= xes[r - 1][c - 1]
                    yes[r][c] -= yes[r - 1][c - 1]

                match grid[r][c] :
                    case 'X' :
                        xes[r][c] += 1
                    case 'Y' :
                        yes[r][c] += 1

        output = 0
        for x in range(len(grid)) :
            for y in range(len(grid[0])) :
                if xes[x][y] == yes[x][y] and xes[x][y] :
                    output += 1

        return output
