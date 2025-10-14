class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs :
            return s

        class UF :
            def __init__(self, n) :
                self.p = list(range(n))
            def union(self, x, y) :
                self.p[self.find(x)] = self.find(y)
            def find(self, x) :
                if x != self.p[x] :
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        # Union Find
        uf = UF(len(s))
        for x, y in pairs :
            uf.union(x, y)

        # Grouping UF Results
        groups = {}
        for i, x in enumerate(s) :
            g = uf.find(i)
            if g not in groups :
                # [indexes, values]
                groups[g] = [[], []]
            groups[g][0].append(i)
            groups[g][1].append(x)

        # Compiling output
        output = [None] * len(s)
        for indxs, vals in groups.values() :
            vals.sort()
            for i, v in zip(indxs, vals) :
                output[i] = v

        return ''.join(output)