class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        current = set(nums[0])
        for i in range(1, len(nums)) :
            current = current.intersection(set(nums[i]))

        return sorted(list(current))    