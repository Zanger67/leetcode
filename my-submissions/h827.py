# grid value: 0 | 1 ===>>> new grid value: -(island_id)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # Count grid tiles and set the new grid tile to be a negative 
        # value: the island's assigned ID but negative
        # This marks islands as visited
        def propogate_grid(r: int, c: int, grid: List[List[int]], island_id: int) -> int :
            grid[r][c] = -island_id
            size = 1
            if r > 0 and grid[r - 1][c] > 0 :
                size += propogate_grid(r - 1, c, grid, island_id)
            if r < len(grid) - 1 and grid[r + 1][c] > 0 :
                size += propogate_grid(r + 1, c, grid, island_id)
            if c > 0 and grid[r][c - 1] > 0 :
                size += propogate_grid(r, c - 1, grid, island_id)
            if c < len(grid[0]) - 1 and grid[r][c + 1] > 0 :
                size += propogate_grid(r, c + 1, grid, island_id)
            return size

        maxx_island = 0
        island_id_counter = 1
        island_sizes = {}               # {island_id: size}
        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] > 0 :
                    island_size = propogate_grid(r, c, grid, island_id_counter)
                    island_sizes[island_id_counter] = island_size
                    maxx_island = max(maxx_island, island_size)
                    island_id_counter += 1

        # If the entire grid is occupied, that's the max size
        # If not, then we can at least add one tile to the largest
        # island e.g. if there's only one island
        if maxx_island == len(grid) * len(grid[0]) :
            return maxx_island
        else :
            maxx_island += 1

        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] == 0 :
                    large_island = 1
                    ids = set()                         # We don't want to add an island twice
                    if r > 0 and grid[r - 1][c] :
                        ids.add(grid[r - 1][c])
                        large_island += island_sizes[-grid[r - 1][c]]
                    if r < len(grid) - 1 and grid[r + 1][c] and grid[r + 1][c] not in ids :
                        ids.add(grid[r + 1][c])
                        large_island += island_sizes[-grid[r + 1][c]]
                    if c > 0 and grid[r][c - 1] and grid[r][c - 1] not in ids :
                        ids.add(grid[r][c - 1])
                        large_island += island_sizes[-grid[r][c - 1]]
                    if c < len(grid[0]) - 1 and grid[r][c + 1] and grid[r][c + 1] not in ids :
                        large_island += island_sizes[-grid[r][c + 1]]
                    maxx_island = max(maxx_island, large_island)

        return maxx_island