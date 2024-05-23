# https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumapp = sum(apple)
        heapq._heapify_max(capacity)

        counter = 0
        while sumapp > 0 :
            sumapp -= heapq._heappop_max(capacity)
            counter += 1
        return counter