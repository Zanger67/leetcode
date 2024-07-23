''' Notes
    Discount total = total cost - (top DISCOUNT costs / 2)
'''

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        hp = [(0, discounts, 0)]   # schema: (cumu cost, discounts, city)

        path = [[] for _ in range(n)]
        for c1, c2, toll in highways :
            path[c1].append((c2, toll))
            path[c2].append((c1, toll))

        cityCosts = [{} for _ in range(n)]
        cityCosts[0][0] = 0

        while hp :
            cost, discRem, city = heapq.heappop(hp)

            if city == n - 1 :
                return cost

            if cost > cityCosts[city].get(discRem, inf) :
                continue

            for nxtCity, toll in path[city] :
                if cost + toll < cityCosts[nxtCity].get(discRem, inf) :
                    cityCosts[nxtCity][discRem] = cost + toll
                    heapq.heappush(hp, (cost + toll, discRem, nxtCity))
                if discRem and cost + toll // 2 < cityCosts[nxtCity].get(discRem - 1, inf) :
                    cityCosts[nxtCity][discRem - 1] = cost + toll // 2
                    heapq.heappush(hp, (cost + toll // 2, discRem - 1, nxtCity))

        return -1