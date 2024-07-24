class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        ref = [int(''.join([str(mapping[int(c)]) 
                                    for c in str(x)])) 
                                    for x in nums]

        temp = sorted(zip(nums, ref, range(len(nums))), 
                      key=lambda y: (y[1], y[2]))

        return [x[0] for x in temp]