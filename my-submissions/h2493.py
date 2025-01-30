class Solution:
    # output: (dist, node_no)
    def furthest_vertex(self, curr_node: int, edges: DefaultDict[int, Set[int]], visited: Set[int] = None) -> Tuple[int, int] :
        if not visited :
            visited = set()
        nxt_to_visit = deque([(1, curr_node)])
        farthest = (-1, -1)
        while nxt_to_visit :
            dist, curr = nxt_to_visit.popleft()

            if curr in visited :
                continue
            visited.add(curr)

            if dist > farthest[0] :
                farthest = (dist, curr)

            for nxt in edges[curr] :
                if nxt in visited :
                    continue
                nxt_to_visit.append((dist + 1, nxt))

        return farthest

    def odd_cycle_len(self, 
                      curr_node: int, 
                      traversal_no: int, 
                      edges: DefaultDict[int, Set[int]], 
                      visited: Dict[int, int] = None) -> bool :
        if curr_node in visited :
            return (traversal_no - visited[curr_node]) % 2 != 0

        visited[curr_node] = traversal_no

        return any(self.odd_cycle_len(x, traversal_no + 1, edges, visited) for x in edges[curr_node])

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Edge list from each vertex
        e = defaultdict(set)
        for u, v in edges :
            e[u].add(v)
            e[v].add(u)

        groups = 0

        to_visit = set(range(1, n + 1))
        while to_visit :
            curr = to_visit.pop()

            visited = {}
            if self.odd_cycle_len(curr, 1, e, visited) :
                return -1

            to_visit -= visited.keys()
            groups += max([self.furthest_vertex(x, e) for x in visited.keys()])[0]

        return groups
