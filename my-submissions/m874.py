class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dirr = 'n'
        dirr_r = {x: y for x, y in zip('nesw', 'eswn')}
        dirr_l = {x: y for x, y in zip('nesw', 'wnes')}
        offset = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
        obs = set((x, y) for x, y in obstacles)
        dist = 0

        for c in commands :
            if c == -1 :
                dirr = dirr_r[dirr]
                continue
            if c == -2 :
                dirr = dirr_l[dirr]
                continue

            dx, dy = offset[dirr]
            for _ in repeat(None, c) :
                x_n, y_n = x + dx, y + dy
                if (x_n, y_n) in obs :
                    break
                x, y = x_n, y_n

            dist = max(dist, x ** 2 + y ** 2)

        return dist