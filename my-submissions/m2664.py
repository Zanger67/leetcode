class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        self.options = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]
        self.rem = m * n
        def dfs(x: int,
                y: int,
                output: List[List[int]] = [[-1] * n for _ in range(m)],
                step: int = 0) -> List[int] :
            self.rem -= 1
            output[x][y] = step
            step += 1
            output[x]

            if not self.rem :
                return output

            for a, b in self.options :
                newX, newY = x + a, y + b
                if not (0 <= newX < m) or not (0 <= newY < n) or output[newX][newY] != -1 :
                    continue

                dfs(newX, newY, output, step)
                if not self.rem :
                    return output

            self.rem += 1
            output[x][y] = -1
            return output

        return dfs(r, c)
