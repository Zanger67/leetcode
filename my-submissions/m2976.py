class Solution:
    def minimumCost(self, 
                    source: str, 
                    target: str, 
                    original: List[str], 
                    changed: List[str], 
                    cost: List[int]) -> int:

        # Create mapping of each letter to their cheapest counterparts
        conversions = [{} for _ in range(26)]
        for o, n, c in zip(original, changed, cost) :
            if o == n :
                continue
            if (ord(n) - ord('a')) not in conversions[ord(o) - ord('a')] \
                or conversions[ord(o) - ord('a')][ord(n) - ord('a')] > c :
                conversions[ord(o) - ord('a')][ord(n) - ord('a')] = c

        # Propogate from each point to find all reachable characters
        # and calculate the min cost using Diskstras and a heap.
        for i in range(26) :
            # schema: (cost, target)
            hp = [(c, x) for x, c in conversions[i].items()]
            heapq.heapify(hp)

            while hp :
                c, x = heapq.heappop(hp)
                if x not in conversions[i] or c <= conversions[i][x] :
                    conversions[i][x] = c

                    # from x to target at newCost
                    for tar, newCost in conversions[x].items() :
                        if tar not in conversions[i] \
                            or newCost + c <= conversions[i][tar] :
                            heapq.heappush(hp, (newCost + c, tar))

        # Iterate through the starting string and use the previously
        # computed path-cost mapping to calculate cost
        tot_cost = 0
        for o, c in zip(source, target) :
            if o == c :
                continue
            elif (ord(c) - ord('a')) not in conversions[ord(o) - ord('a')] :
                return -1
            else :
                tot_cost += conversions[ord(o) - ord('a')].get(ord(c) - ord('a'))

        return tot_cost
