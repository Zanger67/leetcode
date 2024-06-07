# Cause funny python "1" (2) liner

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        return [[x for x in cnt if cnt.get(x) >= c] for c in range(1, max(cnt.values()) + 1)]
