class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = nums.count(1)
        if not totalOnes :
            return 0

        oneCount = nums[:totalOnes].count(1)
        zeroCount = totalOnes - oneCount
        minMoves = zeroCount

        for i, nxtVal in enumerate(nums[totalOnes:] + nums[:totalOnes], totalOnes) :
            if nxtVal :
                oneCount += 1
            else :
                zeroCount += 1

            if nums[i - totalOnes] :
                oneCount -= 1
            else :
                zeroCount -= 1

            minMoves = min(minMoves, zeroCount)

        return minMoves
git p