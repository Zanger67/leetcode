class Solution:
    def _dfs_helper(self, curr: int, n: int, edges: defaultdict, path: List[int] = None, output: List[List[int]] = None) -> List[List[int]] :
        if output is None :
            output: List[List[int]] = []

        if path is None :
            path = [curr]

        if curr == n - 1 :
            output.append(path.copy())
            return

        for e in edges[curr] :
            path.append(e)
            self._dfs_helper(e, n, edges, path, output)
            path.pop()

        return output
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self._dfs_helper(0, len(graph), graph)