# https://leetcode.com/problems/remove-element/


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        currentPointer = 0
        for i in range(len(nums)) :
            if not nums[i] == val :
                nums[currentPointer] = nums[i]
                currentPointer += 1
        return currentPointer