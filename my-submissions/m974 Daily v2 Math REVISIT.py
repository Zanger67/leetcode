# I wanna redo this to understand the math

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pastRemainders = {0: 1}
        runningRem = 0
        counter = 0
        for num in nums :
            runningRem = (runningRem + num) % k
            counter += pastRemainders.get(runningRem, 0)
            pastRemainders[runningRem] = pastRemainders.get(runningRem, 0) + 1
        return counter
