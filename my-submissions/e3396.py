class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        above = sum([1 for v in cnt.values() if v > 1])

        for i, c in enumerate(nums) :
            if above == 0 :
                return ceil(i / 3)
            if cnt[c] == 1 :
                cnt.pop(c)
            cnt[c] -= 1
            if cnt[c] == 1 :
                above -= 1

        return ceil(len(nums) / 3)