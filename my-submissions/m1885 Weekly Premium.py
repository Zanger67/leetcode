class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        newNums = sorted([nums1[x] - nums2[x] for x in range(len(nums1))])

        left, right = 0, len(newNums) - 1
        counter = 0
        while (left < right) :
            if (newNums[left] + newNums[right] > 0) :
                counter += right - left
                right -= 1
            else :
                left += 1
        return counter
