class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        routes = [[] for _ in range(n)]

        for a, b, w in edges :
            routes[a].append((b, w))
            routes[b].append((a, w))

        cityWithFewest = inf
        cityNo = -1

        # i = source city
        for i in range(n) :
            visited = set()
            toVisit = [(0, i)]       # heap

            while toVisit :
                dist, currCity = heapq.heappop(toVisit)

                if currCity in visited :
                    continue

                visited.add(currCity)

                for nextCity, w in routes[currCity] :
                    if nextCity not in visited and w + dist <= distanceThreshold :
                        heapq.heappush(toVisit, (w + dist, nextCity))

            if len(visited) - 1 <= cityWithFewest :
                cityWithFewest = len(visited) - 1
                cityNo = i

        return city