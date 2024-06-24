# Intuition: we can basically form any number less than or equal
# to numbers we have, so we can isolate their bits and take
# whichever are present
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        output = 0
        for num in nums :
            output |= num

        return output