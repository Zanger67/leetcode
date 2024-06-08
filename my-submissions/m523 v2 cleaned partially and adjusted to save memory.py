# https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-06-08


''' Notes
    If we have a leftPointer and rightPointer, they can move along
    like a sliding window, adding the new items and subtracting the
    leftmost items.

    This would be at most O(n^2) since C(n, 2) would be
    n!/(2!(n-2)!) aka n^2 (plus n cases where they are 
    the same value but eh still n^2)
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) <= 1 :
            return False

        pastRemainders = {}
        pastRemainders[nums[0] % k] = 1
        prevVal = nums[0] % k

        for i in range(1, len(nums)) :
            newVal = (prevVal + nums[i]) % k

            # since this is a cumulative remainder and manually 
            # do index 0, this is permitted
            if not newVal : 
                return True
            if newVal not in pastRemainders :
                # set as neightbor so if neightbor same prefix, move on
                pastRemainders[newVal] = i + 1
            elif not pastRemainders[newVal] == i:
                return True
            prevVal = newVal

        return False
