# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/

''' Notes:
    Max output will be at most 2x the max reward there is
'''

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues.sort()

        maxx = max(rewardValues)
        helperArr = [True] + [False] * (maxx * 2)

        for reward in rewardValues :
            for j in range(reward - 1, -1, -1) :
                if helperArr[j] :
                    helperArr[j + reward] = True
        
        for i in range(maxx * 2, -1, -1) :
            if helperArr[i] :
                return i
        return -1
