class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.larger = [x for x in sorted(nums, reverse=True)[:k]]     # min heap
        self.k = k
        heapq.heapify(self.larger)

    def add(self, val: int) -> int:
        if len(self.larger) < self.k :
            heapq.heappush(self.larger, val)
            return self.larger[0]

        if val == self.larger[0] :
            return val

        if val > self.larger[0] :
            heapq.heappushpop(self.larger, val)

        return self.larger[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)