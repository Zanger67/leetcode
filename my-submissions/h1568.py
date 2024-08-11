class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def island(i: int, j: int, visited: Set[Tuple[int, int]]) -> None :
            if not (0 <= i < len(grid)) or \
               not (0 <= j < len(grid[0])) or \
               (i, j) in visited or \
               not grid[i][j]:
                return

            visited.add((i, j))
            island(i - 1, j, visited)
            island(i + 1, j, visited)
            island(i, j - 1, visited)
            island(i, j + 1, visited)

        def moreThanOneIsland(x: int, y: int) -> bool :
            islandFnd = False
            visited = set([(x, y)])
            for i in range(len(grid)) :
                for j in range(len(grid[0])) :
                    if grid[i][j] and (i, j) not in visited  :
                        if islandFnd :
                            return True
                        island(i, j, visited)
                        islandFnd = True

            return not islandFnd

        if moreThanOneIsland(-1, -1) :
            return 0

        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] and moreThanOneIsland(i, j) :
                    return 1

        return 2
