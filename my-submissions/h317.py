class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        dist_grid = [[0 if x == 0 else inf for x in r] for r in grid]

        for x in range(len(grid)) :
            for y in range(len(grid[0])) :
                if grid[x][y] != 1 :
                    continue
                self._bfs_propogater(x, y, grid, dist_grid)


        output = inf
        for r in zip(grid, dist_grid) :
            for orig, out_val in zip(r[0], r[1]) :
                if orig == 0 :
                    output = min(output, out_val)

        if output is None or output == inf :
            return -1
        return output

    def _bfs_propogater(self, x: int, y: int, 
                        grid: List[List[int]], 
                        dist_grid: List[List[int]]) :
        nexts = deque([(x, y, 0)])
        offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set([(x, y)])
        while nexts :
            x_curr, y_curr, dist = nexts.popleft()
            dist_grid[x_curr][y_curr] += dist
            dist += 1
            for dx, dy in offsets :
                x_new, y_new = x_curr + dx, y_curr + dy
                if (0 <= x_new < len(grid) and 
                    0 <= y_new < len(grid[0]) and 
                    (x_new, y_new) not in visited and 
                    grid[x_new][y_new] == 0) :
                    visited.add((x_new, y_new))
                    nexts.append((x_new, y_new, dist))

        for x2 in range(len(grid)) :
            for y2 in range(len(grid[0])) :
                if (x2, y2) not in visited :
                    dist_grid[x2][y2] = inf