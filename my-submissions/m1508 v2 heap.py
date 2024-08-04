class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hp = []

        for i in range(len(nums)) :
            currSum = 0
            for j in range(i, len(nums)) :
                currSum += nums[j]
                heapq.heappush(hp, currSum)
        
        output = 0
        for i in range(left - 1) :
            heapq.heappop(hp)
        for i in range(left - 1, right) :
            output += heapq.heappop(hp)

        return output % (10 ** 9 + 7)