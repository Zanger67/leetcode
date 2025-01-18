class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def add_case(moves: int, x_new: int, y_new: int) -> None :
            if 0 <= x_new < len(grid) and \
               0 <= y_new < len(grid[0]) and \
               grid[x_new][y_new] < 10:
                heapq.heappush(next_check, (moves, x_new, y_new))

        next_check = [(10, 0, 0)]     # (moves, x, y)

        while next_check :
            moves, x, y = heapq.heappop(next_check)

            if grid[x][y] >= 10:
                continue

            if x == len(grid) - 1 and y == len(grid[0]) - 1 :
                return moves - 10

            dirr, grid[x][y] = grid[x][y], moves

            # direction
            match dirr :
                case 1 :                            # right grid[i][j + 1]
                    add_case(moves, x, y + 1)
                    add_case(moves + 1, x + 1, y)
                    add_case(moves + 1, x - 1, y)
                    add_case(moves + 1, x, y - 1)
                case 2 :                            # left grid[i][j - 1]
                    add_case(moves, x, y - 1)
                    add_case(moves + 1, x + 1, y)
                    add_case(moves + 1, x - 1, y)
                    add_case(moves + 1, x, y + 1)
                case 3 :                            # down grid[i + 1][j]
                    add_case(moves, x + 1, y)
                    add_case(moves + 1, x - 1, y)
                    add_case(moves + 1, x, y + 1)
                    add_case(moves + 1, x, y - 1)
                case 4 :                            # up grid[i - 1][j]
                    add_case(moves, x - 1, y)
                    add_case(moves + 1, x + 1, y)
                    add_case(moves + 1, x, y + 1)
                    add_case(moves + 1, x, y - 1)

        return -1