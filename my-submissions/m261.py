class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1 :
            return False

        # Create edge map
        e = defaultdict(set)
        for u, v in edges :
            e[u].add(v)
            e[v].add(u)

        # Detect cycle to save runtime -- breaks out early if cycle detected otherwise attempts
        # to validate by visiting all n edges
        def dfs_detect_cycle(curr: int, prev: int, e: defaultdict, visited: Set[int]) -> bool :
            if curr in visited :
                return True
            visited.add(curr)
            if any(dfs_detect_cycle(nxt, curr, e, visited) for nxt in e[curr] if nxt != prev) :
                return (True, visited)
            return False

        # Since dfs_detect_cycle() is called first before the or, visited() will be
        # filled prior to len() being tested
        visited = set()
        if dfs_detect_cycle(1, None, e, visited) or not len(visited) == n :
            return False

        return True