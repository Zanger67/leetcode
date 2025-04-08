class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        e = defaultdict(list)
        for u, v in edges :
            e[u].append(v)
            e[v].append(u)
        to_visit = set(range(0, n))

        output = 0
        while to_visit :
            to_visit.add((nxt := [to_visit.pop()])[0])
            output += 1

            while nxt :
                if (curr := nxt.pop()) not in to_visit :
                    continue
                to_visit.remove(curr)
                nxt.extend(x for x in e[curr] if x in to_visit)

        return output