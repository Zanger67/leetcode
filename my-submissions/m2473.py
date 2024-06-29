class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        travelCostMultiplier = k + 1
        output = []

        roadChoices = defaultdict(list)

        for road in roads :
            roadChoices[road[0]].append((road[1], road[2]))
            roadChoices[road[1]].append((road[0], road[2]))

        for i in range(1, n + 1) :
            toVisit = []            # (totalRoadCost, targetIndx)
            toVisit.append((0, i))
            distances = [inf] * n

            while toVisit :
                cost, node = heapq.heappop(toVisit)
                if distances[node - 1] != inf :
                    continue

                distances[node - 1] = cost

                for nextNode, additionalCost in roadChoices[node] :
                    heapq.heappush(toVisit, (cost + additionalCost, nextNode))
            
            output.append(min([distances[x] * travelCostMultiplier + appleCost[x] for x in range(n)]))
        
        return output

