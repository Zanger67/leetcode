class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def dfs(r: int, 
                c: int, 
                qaud: str, 
                visited: Set[Tuple[int, int, int]],
                grid: List[str]) -> None :
            if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) :
                return
            if (r, c) in visited :
                return
            if (r, c, qaud) in visited :
                return

            if grid[r][c] == ' ' :
                visited.add((r, c))
                dfs(r - 1, c, 'D', visited, grid)
                dfs(r + 1, c, 'U', visited, grid)
                dfs(r, c - 1, 'R', visited, grid)
                dfs(r, c + 1, 'L', visited, grid)
                return

            visited.add((r, c, qaud))
            if grid[r][c] == '/' :
                if qaud == 'U' or qaud == 'L' :
                    dfs(r, c, 'U', visited, grid)
                    dfs(r, c, 'L', visited, grid)
                    dfs(r, c - 1, 'R', visited, grid)
                    dfs(r - 1, c, 'D', visited, grid)
                else :
                    dfs(r, c, 'D', visited, grid)
                    dfs(r, c, 'R', visited, grid)
                    dfs(r, c + 1, 'L', visited, grid)
                    dfs(r + 1, c, 'U', visited, grid)
            else : # \\
                if qaud == 'U' or qaud == 'R' :
                    dfs(r, c, 'U', visited, grid)
                    dfs(r, c, 'R', visited, grid)
                    dfs(r, c + 1, 'L', visited, grid)
                    dfs(r - 1, c, 'D', visited, grid)
                else : # L/D
                    dfs(r, c, 'L', visited, grid)
                    dfs(r, c, 'D', visited, grid)
                    dfs(r, c - 1, 'R', visited, grid)
                    dfs(r + 1, c, 'U', visited, grid)

        grid = [x.replace('\\', '.') for x in grid]

        visited = set()
        counter = 0
        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                for i in ['R', 'L', 'U', 'D'] :
                    if (r, c, i) in visited or (r, c) in visited:
                        continue
                    counter += 1
                    dfs(r, c, i, visited, grid)

        return counter