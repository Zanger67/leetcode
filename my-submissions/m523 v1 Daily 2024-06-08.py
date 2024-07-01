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
        pastRemainders[nums[0] % k] = 0
        nums[0] %= k
        for i in range(1, len(nums)) :
            nums[i] = (nums[i - 1] + nums[i]) % k
            if not nums[i] :
                return True
            if nums[i] not in pastRemainders :
                pastRemainders[nums[i]] = i
                continue
            if pastRemainders[nums[i]] < i - 1 :
                return True

        return False





    
    # def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    #     if len(nums) <= 1 :
    #         return False
    #     # To calculate the remainder val of left, right, we take
    #     # nums[right] - nums[left - 1] (defaulting to 0 if out of bounds) 
    #     helperVals = [0]
    #     for i in range(len(nums)) :
    #         helperVals.append((helperVals[i] + nums[i]) % k)
    #         if helperVals[-1] == 0 :
    #             return True

    #     self.seenSums = set()

    #     print(nums)
    #     print([x % k for x in nums])
    #     print(helperVals)
    #     print(len(helperVals))
    #     return self.helper(helperVals, k, 1, 2)

    # def helper(self, nums, k, left, right) -> bool :
    #     if right <= left :
    #         return False
    #     if right >= len(nums) :
    #         return False

    #     if ((nums[right] - nums[left - 1]) % k) in self.seenSums :
    #         return True
        
    #     self.seenSums.add((nums[right] - nums[left - 1]) % k)

    #     # print(left, right)
    #     return ((nums[right] - nums[left - 1]) % k == 0) or \
    #             self.helper(nums, k, left + 1, right) or \
    #             self.helper(nums, k, left, right + 1)        

    # def helper(self, nums, k, left, right, currentSum) -> bool :
    #     # print(left, right, currentSum)
    #     if right - left < 1 :
    #         # print(f'FALSE\tleft: {left}, right: {right}, currentSum: {currentSum}')
    #         return False
    #     if right >= len(nums) :
    #         # print(f'FALSE\tleft: {left}, right: {right}, currentSum: {currentSum}')
    #         return False
    #     if currentSum % k == 0:
    #         # print(f'TRUE\tleft: {left}, right: {right}, currentSum: {currentSum}')
    #         return True
    #     # print('False. Moving on')
    #     if self.helper(nums, k, left + 1, right, currentSum - nums[left]) :
    #         return True
    #     if right + 1 >= len(nums) :
    #         return False
    #     else :
    #         return self.helper(nums, k, left, right + 1, currentSum + nums[right + 1])