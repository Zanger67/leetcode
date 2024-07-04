# CONSTANT Extra Space
# Must be O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorVal = 0
        for i in nums :
            xorVal ^= i

        refVal = xorVal
        divBy = 1 
        while refVal % 2 == 0 :
            refVal = refVal // 2
            divBy *= 2
        refVal = (refVal % 2) * divBy

        val1, val2 = 0, 0        
        for i in nums :
            if refVal & i :
                val1 ^= i
            else :
                val2 ^= i
            
                
        return [val1, val2]

        