class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        paths = defaultdict(list)

        for u, v in edges :
            paths[u].append(v)
            paths[v].append(u)

        dist1 = [0] + [inf] * n
        dist2 = dist1.copy()


        # schema: (time when reached, current node no.)
        toVisit = [(0, 1)]
        while toVisit :
            currTime, curr = heapq.heappop(toVisit)

            # If first case and second case already found
            if dist1[curr] != inf and dist2[curr] != inf :
                continue
            # Repeat distance
            if currTime == dist1[curr] :
                continue

            # If not found so insert
            if dist1[curr] == inf :
                dist1[curr] = currTime
            else :
                dist2[curr] = currTime

            # If "red light," adjust time
            if currTime % (2 * change) >= change :
                nxtTime = currTime + time + change - (currTime % change)
            else :
                nxtTime = currTime + time

            # Add future cases
            for nxt in paths[curr] :
                heapq.heappush(toVisit, (nxtTime, nxt))

        return dist2[-1]

