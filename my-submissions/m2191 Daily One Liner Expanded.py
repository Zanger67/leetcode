class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return [
            z[0] for z in 
                sorted(
                    zip(
                        nums,
                        [int(''.join([str(mapping[int(c)]) for c in str(x)])) for x in nums],
                        range(len(nums))
                    ),
                    key=lambda y: (y[1], y[2]))
            ]