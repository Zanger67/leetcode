class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        output, cumsum = 0, 0
        left, right = 0, 0

        right_up = True
        while right < len(nums) :
            if left > right :
                right += 1
                cumsum, right_up = 0, True
                continue

            if right_up :
                cumsum += nums[right]

            if cumsum * (right - left + 1) >= k :
                cumsum -= nums[left]
                right_up = False
                left += 1
                continue

            right += 1
            output += right - left
            right_up = True

        return output