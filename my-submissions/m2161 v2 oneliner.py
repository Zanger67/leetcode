class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return sorted(nums, key=lambda x: (x < pivot, x == pivot), reverse=True)