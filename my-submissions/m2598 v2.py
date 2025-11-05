class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mods = Counter([num % value for num in nums])
        minn = min(mods[x] for x in range(value))
        additional = 0

        while mods[additional] != minn :
            additional += 1

        return minn * value + additional