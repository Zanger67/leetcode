# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right :
            difference = target - numbers[right]
            
            if numbers[left] == difference :
                break
            
            if difference < numbers[left] :
                right -= 1
            else :
                left += 1

        return [left + 1, right + 1]