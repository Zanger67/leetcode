class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        hp = [(0, discounts, 0)]   # schema: (cumu cost, discounts, city)

        path = [[] for _ in range(n)]
        for c1, c2, toll in highways :
            path[c1].append((c2, toll))
            path[c2].append((c1, toll))

        visited = [[] for _ in range(n)] # schema: [(cost, discounts)]
        targetCost = -1

        while hp :
            cost, discLeft, city = heapq.heappop(hp)

            # End city reached so go no further
            if city == n - 1 :
                if targetCost == -1 or targetCost > cost :
                    targetCost = cost
                continue

            # Check if "favourable" case
            cont = False
            if visited[city] :
                for c, d in visited[city] :
                    if d >= discLeft and cost >= c :
                        cont = True
                        break

            if cont :
                continue
            visited[city].append((cost, discLeft))

            for nextCity, toll in path[city] :
                heapq.heappush(hp, (cost + toll, discLeft, nextCity))
                if discLeft :
                    heapq.heappush(hp, (cost + (toll // 2), discLeft - 1, nextCity))

        return targetCost