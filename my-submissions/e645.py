class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        correctSum = ((1 + len(nums)) * len(nums)) // 2
        currentSum = sum(nums)
        dupeVal = -1
        pastVals = set()

        for i in range(0, len(nums)) :
            if nums[i] in pastVals :
                dupeVal = nums[i]
                break
            pastVals.add(nums[i])

        print(dupeVal, correctSum, currentSum)
        missingVal = dupeVal + correctSum - currentSum

        return [dupeVal, missingVal]