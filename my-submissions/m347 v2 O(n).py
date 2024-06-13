# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        cnt = Counter(nums)

        # O(n) reversal worst case
        revCnt = {}
        maxx = 0
        for key, val in cnt.items() :
            maxx = max(maxx, val)
            if val in revCnt :
                revCnt[val].append(key)
            else :
                revCnt[val] = [key]

        # O(n) worst case k == n
        output = []
        while maxx >= 0 and k > 0 :
            if maxx not in revCnt or not revCnt[maxx] :
                maxx -= 1
                continue
            output.append(revCnt[maxx].pop())
            k -= 1

        return output