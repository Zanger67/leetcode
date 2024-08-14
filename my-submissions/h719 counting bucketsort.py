class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        buckets = [0 for _ in range(max(nums) + 1)]

        for i, v in enumerate(nums[:-1]) :
            for u in nums[i + 1:] :
                buckets[abs(u - v)] += 1

        indx = 0
        while k > buckets[indx] :
            k -= buckets[indx]
            indx += 1
        return indx
