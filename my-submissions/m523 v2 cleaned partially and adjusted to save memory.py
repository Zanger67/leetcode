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
