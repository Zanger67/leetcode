class Solution:
    def traverse_waterpocket(self, r: int, c: int, grid: List[List[int]]) -> int :
        output, grid[r][c] = grid[r][c], 0
        if r - 1 >= 0 and grid[r - 1][c] :
            output += self.traverse_waterpocket(r - 1, c, grid)
        if c - 1 >= 0 and grid[r][c - 1] :
            output += self.traverse_waterpocket(r, c - 1, grid)
        if r + 1 < len(grid) and grid[r + 1][c] :
            output += self.traverse_waterpocket(r + 1, c, grid)
        if c + 1 < len(grid[0]) and grid[r][c + 1] :
            output += self.traverse_waterpocket(r, c + 1, grid)
        return output

    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxx = 0

        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if not grid[r][c] :
                    continue
                maxx = max(maxx, self.traverse_waterpocket(r, c, grid))

        return maxx