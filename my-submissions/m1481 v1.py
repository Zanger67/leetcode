class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        cnt = Counter(arr)

        # Sort so that lease frequent are at the end, groupped by their value
        arr.sort(reverse=True, key=lambda x: (cnt.get(x), x))

        for _ in range(k) :
            poppedVal = arr.pop()
            if cnt.get(poppedVal) == 1 :
                cnt.pop(poppedVal)
            else :
                cnt[poppedVal] = cnt.get(poppedVal) - 1
        
        return len(cnt)