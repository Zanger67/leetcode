class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 :
            return nums[0]
            
        hp = [(-nums[0], 0)]
        for i in range(1, len(nums) - 1) :
            while hp[0][1] < i - k :
                heapq.heappop(hp)
            heapq.heappush(hp, (-nums[i] + hp[0][0], i))

        while hp[0][1] < len(nums) - 1 - k :
            heapq.heappop(hp)

        return -hp[0][0] + nums[-1]