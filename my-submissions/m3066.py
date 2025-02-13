class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2 :
            a, b = heappop(nums), heappop(nums)

            if a >= k and b >= k :
                return ops
            heappush(nums, max(a, b) + 2 * min(a, b))
            ops += 1

        return ops

