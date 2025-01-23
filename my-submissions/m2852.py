class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        def helper(r: int, c: int, output_vals: List[int] = None) -> List[int] :
            if not output_vals :
                output_vals = [0, 0]
            if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) :
                return output_vals
            if grid[r][c] == -1 :
                return output_vals

            output_vals[0] += 1
            output_vals[1] += grid[r][c]
            grid[r][c] = -1

            helper(r + 1, c, output_vals)
            helper(r - 1, c, output_vals)
            helper(r, c + 1, output_vals)
            helper(r, c - 1, output_vals)

            return output_vals

        island_sums = []

        for r in range(len(grid)) :
            for c in range(len(grid[0])) :
                if grid[r][c] == -1 :
                    continue
                island_sums.append(helper(r, c))

        output = 0
        tot_sum = sum([x[1] for x in island_sums])

        for x in island_sums :
            output += (tot_sum - x[1]) * x[0]


        return output