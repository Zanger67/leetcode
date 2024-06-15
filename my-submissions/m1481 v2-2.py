class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)

        # We don't care which values we pop, just that we do it greedily
        cntValues = sorted([freq for freq in cnt.values()], reverse=True)

        while k > 0 and cntValues[-1] <= k:
            k -= cntValues.pop()

        return len(cntValues)
