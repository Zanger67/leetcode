class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)

        # We don't care which values we pop, just that we do
        cntValues = sorted([freq for freq in cnt.values()], reverse=True)

        while k > 0 :
            if cntValues[-1] <= k :     # we can keep popping
                k -= cntValues.pop()
            else :                      # we can pop no longer
                break

        return len(cntValues)
