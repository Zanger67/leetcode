# https://leetcode.com/problems/find-subarrays-with-equal-sum/description/


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumsSet = set()

        for i in range(0, len(nums) - 1) :
            sum = nums[i] + nums[i + 1]
            
            if (sum in sumsSet) :
                return True
            
            sumsSet.add(sum)
        
        return False