class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = defaultdict(set), defaultdict(set)

        for r, row in enumerate(grid) :
            for c, cell in enumerate(row) :
                if not cell :
                    continue

                rows[r].add(c)
                cols[c].add(r)

        output = sum([len(cnt) for r, cnt in rows.items() if len(cnt) > 1]) + \
                 sum([len(cnt) for c, cnt in cols.items() if len(cnt) > 1])

        for r, row in enumerate(grid) :
            for c, cell in enumerate(row) :
                if not cell :
                    continue
                if len(rows[r]) > 1 and len(cols[c]) > 1 :
                    output -= 1

        return output