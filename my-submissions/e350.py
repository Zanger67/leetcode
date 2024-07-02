class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt = Counter(nums1) & Counter(nums2)
        output = []
        for i, val in cnt.items() :
            output.extend([i] * val)

        return output