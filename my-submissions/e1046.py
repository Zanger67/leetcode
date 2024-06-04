# https://leetcode.com/problems/last-stone-weight/description/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneCount = len(stones)
        heapq._heapify_max(stones)

        while stoneCount > 1 :
            stoneOne = heapq._heappop_max(stones)
            stoneTwo = heapq._heappop_max(stones)
            result = abs(stoneOne - stoneTwo)

            if result == 0 :
                stoneCount -= 2
            else :
                stoneCount -= 1
                heapq.heappush(stones, result)
                heapq._heapify_max(stones)
        
        return 0 if len(stones) == 0 else stones[0]