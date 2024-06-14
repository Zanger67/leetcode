# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        prevVals = set()
        maxVal = -inf
        output = 0
        for num in nums :
            if num in prevVals :
                maxVal = maxVal + 1
                output += maxVal - num
                prevVals.add(maxVal)
            else :
                maxVal = num
                prevVals.add(num)

        return output
