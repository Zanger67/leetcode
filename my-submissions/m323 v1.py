class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        e = defaultdict(list)
        for u, v in edges :
            e[u].append(v)
            e[v].append(u)
        to_visit = set(range(0, n))

        output = 0
        while to_visit :
            visited = set()
            nxt = [to_visit.pop()]
            output += 1

            while nxt :
                curr = nxt.pop()
                if curr in visited :
                    continue
                visited.add(curr)
                for x in e[curr] :
                    if x not in visited :
                        nxt.append(x)
            to_visit -= visited

        return output