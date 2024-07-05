class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.larger = [x for x in nums[:k]]     # min heap
        self.smaller = [-x for x in nums[k:]]   # max heap
        self.k = k

        heapq.heapify(self.smaller)
        heapq.heapify(self.larger)

    def add(self, val: int) -> int:
        if len(self.larger) < self.k :
            heapq.heappush(self.larger, val)
            return self.larger[0]
        if self.larger and val == self.larger[0] :
            return val

        if self.larger and val > self.larger[0] :
            transfer = heapq.heappushpop(self.larger, val)
            heapq.heappush(self.smaller, -transfer)
            return self.larger[0]

        heapq.heappush(self.smaller, -val)
        return self.larger[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)