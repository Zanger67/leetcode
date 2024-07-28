class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        reached = [True] + [False for _ in range(n)]

        adj = defaultdict(list)
        for u, v, w in times :
            adj[u].append((v, w))
        
        # (delay when reached, node reached)
        toVisit = [(0, k)]
        maxDelay = 0
        while toVisit :
            delay, curr = heapq.heappop(toVisit)

            if reached[curr] :
                continue

            maxDelay = delay
            reached[curr] = True

            for nxt, w in adj[curr] :
                # This if statement is in theory doubled
                # but provides benefits if a node is queued up
                # in the PQ twice
                if not reached[nxt] :
                    heapq.heappush(toVisit, (delay + w, nxt))

        if any(not x for x in reached) :
            return -1
        return maxDelay