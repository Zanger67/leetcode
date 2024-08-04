class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        hp = []

        for i in range(len(nums)) :
            currSum = 0
            for j in range(i, len(nums)) :
                currSum += nums[j]
                hp.append(currSum)

        hp.sort()

        return sum(hp[left-1:right]) % (10 ** 9 + 7)