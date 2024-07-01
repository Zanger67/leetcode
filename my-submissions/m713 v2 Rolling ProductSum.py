class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        current = nums[0]

        counter = 0
        left, right = 0, 0

        while right < len(nums) :
            if (current < k) :
                counter += right - left + 1
                right += 1
                if right < len(nums) :
                    current *= nums[right]
            else :
                current //= nums[left]
                left += 1
                if left > right :
                    right += 1
                    if right < len(nums) :
                        current *= nums[right]

        return counter