class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        usableVals = []

        # zip of (profits, capital) sorted by capital
        # Profits are negative for later use since heapq is a minheap
        capitalAndProfits = sorted([(-1 * p, c) for p, c in zip(profits, capital)], 
                                    reverse=True, 
                                    key=lambda x : x[1])
        

        for i in range(k) :
            while capitalAndProfits and capitalAndProfits[-1][1] <= w :
                # Since profit is first, it will prioritize profits
                heapq.heappush(usableVals, capitalAndProfits.pop())

            if not usableVals :
                return w
            
            w -= heapq.heappop(usableVals)[0]   # subtract the negative profit

        return w
