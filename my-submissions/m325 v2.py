class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prev = {0: -1}
        output, curr_sum = 0, 0

        for i, x in enumerate(nums) :
            curr_sum += x
            if curr_sum - k in prev :   # Check prefix sum for possible k match
                output = max(output, i - prev[curr_sum - k])
            if curr_sum not in prev :   # First occurance will always be farthest / longest
                prev[curr_sum] = i

        return output