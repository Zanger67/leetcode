class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        heap = [(-profit[i], difficulty[i]) for i in range(len(difficulty))]
        heapq.heapify(heap)

        worker.sort()

        output = 0
        while worker and heap:
            if worker[-1] >= heap[0][1] :
                output += -heap[0][0]
                worker.pop()
            else :
                heapq.heappop(heap)

        return output