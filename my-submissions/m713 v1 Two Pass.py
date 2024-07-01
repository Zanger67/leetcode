class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        nums2 = [1] + [0] * len(nums)

        for i in range(0, len(nums)) :
            nums2[i + 1] = nums[i] * nums2[i]

        counter = 0
        left, right = 0, 1

        while right < len(nums2) :
            if (nums2[right] / nums2[left] < k) :
                counter += right - left
                right += 1
            else :
                left += 1
                if left >= right :
                    right += 1

        return counter