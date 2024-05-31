# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/


# Solution is O(n) both space and time
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # for O(1) lookups
        referenceDict = {}

        for i in arr :
            if i - difference in referenceDict.keys() :
                referenceDict[i] = 1 + referenceDict[i - difference]
            else :
                referenceDict[i] = 1
            
        return max(referenceDict.values())
        



        # Old attempt that was TLE
        # visited = {}

        # @cache
        # def findLongest(currentIndex: int) -> int:
        #     pointer = currentIndex - 1
        #     while pointer >= 0 :
        #         if arr[currentIndex] - arr[pointer] == difference :
        #             return findLongest(pointer) + 1
        #         pointer -= 1
        #     return 1
        
        # maxx = 0
        # for i in range(len(arr) - 1, -1, -1):
        #     if i in visited.keys():
        #         continue
        #     maxx = max(findLongest(i), maxx)

        # return maxx