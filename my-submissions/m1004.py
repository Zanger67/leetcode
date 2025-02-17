class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        zeros = 0

        maxx = 0
        for right, num in enumerate(nums) :
            if not num :
                zeros += 1

            if zeros > k :
                while left <= right and nums[left] != 0 :
                    left += 1
                zeros -= 1
                left += 1

            if maxx < right - left + 1 :
                maxx = right - left + 1

        return maxx