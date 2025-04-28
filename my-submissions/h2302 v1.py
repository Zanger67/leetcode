class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        output = 0
        tot_sum = 0
        left, right = 0, 0
        right_up = True
        while right < len(nums) :
            if left > right :
                right += 1
                tot_sum = 0
                right_up = True
                continue
            if right_up :
                tot_sum += nums[right]
            if tot_sum * (right - left + 1) >= k :
                tot_sum -= nums[left]
                right_up = False
                left += 1
                continue
            right += 1
            output += right - left
            right_up = True
        return output