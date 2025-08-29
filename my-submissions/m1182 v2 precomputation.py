class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        precomp = [[inf] * len(colors) for _ in range(3)]

        closest = [inf, inf, inf]
        for i, c in enumerate(colors) :
            closest[c - 1] = i
            precomp[0][i] = abs(i - closest[0])
            precomp[1][i] = abs(i - closest[1])
            precomp[2][i] = abs(i - closest[2])
        
        closest = [inf, inf, inf]
        for i in range(len(colors) - 1, -1, -1) :
            closest[colors[i] - 1] = i
            precomp[0][i] = min(precomp[0][i], closest[0] - i)
            precomp[1][i] = min(precomp[1][i], closest[1] - i)
            precomp[2][i] = min(precomp[2][i], closest[2] - i)
        
        for r in precomp :
            for i in range(len(r)) :
                if r[i] == inf :
                    r[i] = -1
        
        return [precomp[c - 1][x] for x, c in queries]