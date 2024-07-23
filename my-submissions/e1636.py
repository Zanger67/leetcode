class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted([x for x in nums], key=lambda x: (cnt[x], -x))