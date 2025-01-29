class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edges_n = defaultdict(set)
        for u, v in edges :
            edges_n[u].add(v)
            edges_n[v].add(u)


        # return nodes that are in the graph's cycle
        def dfs_find_cycle_nodes(curr: int, 
                                 prev: int, 
                                 stk: List[int], 
                                 visited: Set[int], 
                                 edges: defaultdict) -> List[int] :
            if curr in visited :
                return stk[stk.index(curr):]
            visited.add(curr)
            stk.append(curr)

            for nxt in edges[curr] :
                if nxt == prev :
                    continue

                output = dfs_find_cycle_nodes(nxt, curr, stk, visited, edges)
                if output :
                    return output

            visited.remove(curr)
            stk.pop()
            return None

        cycle_edges = set(dfs_find_cycle_nodes(1, None, [], set(), edges_n))

        for u, v in reversed(edges) :
            if u in cycle_edges and v in cycle_edges :
                return [u, v]

        return None