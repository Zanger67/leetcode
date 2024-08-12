class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges :
            adj[u].append(v)
            adj[v].append(u)

        def dfs(adj: defaultdict, 
                curr: int = 0, 
                prev: int = -1) -> Tuple[int, int] : # (size of subtree, count)

            if curr > len(edges) :
                return (0, 0)

            output = 0
            size = 1
            vals = set()
            for nxt in adj[curr] :
                if nxt == prev :
                    continue
                brchSize, cnt = dfs(adj, nxt, curr)
                output += cnt
                vals.add(brchSize)
                size += brchSize

            if len(vals) <= 1 :
                output += 1
            return (size, output)

        return dfs(adj)[1]
