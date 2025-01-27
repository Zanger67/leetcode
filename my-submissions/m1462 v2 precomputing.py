class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = defaultdict(set)

        for a, b in prerequisites :
            prereqs[b].add(a)

        for k in range(numCourses) :
            to_visit = prereqs[k].copy()
            visited = set()
            while to_visit :
                curr = to_visit.pop()
                if curr in visited :
                    continue
                visited.add(curr)
                prereqs[k].add(curr)
                for nxt in prereqs[curr] :
                    if nxt not in visited :
                        to_visit.add(nxt)

        return [a in prereqs[b] for a, b in queries]