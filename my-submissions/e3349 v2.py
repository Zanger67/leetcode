class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        rem = k - 1
        for i in range(k + 1, len(nums)) :
            if rem == 0 :
                return True
            success = nums[i] > nums[i - 1] and nums[i - k] > nums[i - k - 1]
            rem = rem - 1 if success else k - 1
        return rem == 0