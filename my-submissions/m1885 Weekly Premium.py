class Solution:
    ''' Idea:
        nums1[i] + nums1[j] > nums2[i] + nums2[j]
        ==> nums1[i] - nums2[i] + nums1[j] - nums2[j] > 0
        so we can find the difference array first
        ==> newNums[i] + newNums[j] > 0
        then find how many pairs of values are positive. This would be max n^2 + n?
    '''
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
