class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        inc = []
        curr = 1
        for i in range(1, len(nums)) :
            if nums[i] > nums[i - 1] :
                curr += 1
                continue
            inc.append(curr)
            curr = 1
        inc.append(curr)
        return max([min(x, y) for x, y in zip(inc, inc[1:])] + [max(inc) // 2])