class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return (reduce(xor, map(int, nums1)) if len(nums2) % 2 else 0) ^ (reduce(xor, map(int, nums2)) if len(nums1) % 2 else 0)