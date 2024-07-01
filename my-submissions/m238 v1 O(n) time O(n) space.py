# Question restriction: Must be O(n) and CANNOT use division
# This is O(n) time, O(n) space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n)
        numsLeftProd = [1] + nums.copy()
        numsRightProd = nums.copy() + [1]

        # O(n)
        for i in range(1, len(numsLeftProd)) :
            numsLeftProd[i] *= numsLeftProd[i - 1]

        # O(n)
        for i in range(len(numsRightProd) - 2, -1, -1) : 
            numsRightProd[i] *= numsRightProd[i + 1]
        
        # O(n)
        output = []
        for i in range(len(nums)) :
            output.append(numsLeftProd[i] * numsRightProd[i + 1])

        return output