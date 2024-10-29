class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def dfs(grid: List[List[int]], r: int, c: int) -> int :
            # last column reached
            if c == len(grid[0]) - 1 :
                return 0

            # check for -inf already visited marker
            if grid[r][c] < 0 :
                return 0

            # if any of the next potential squares is valid
            output = 0
            if grid[r][c + 1] > grid[r][c] :
                output = max(output, 1 + dfs(grid, r, c + 1))
            if r < len(grid) - 1 and grid[r + 1][c + 1] > grid[r][c] :
                output = max(output, 1 + dfs(grid, r + 1, c + 1))
            if r > 0 and grid[r - 1][c + 1] > grid[r][c] :
                output = max(output, 1 + dfs(grid, r - 1, c + 1))

            # mark current square as visited since any other that reaches
            # this square will have the same score
            grid[r][c] = -inf

            # return
            return output

        return max([dfs(grid, r, 0) for r in range(len(grid))])
