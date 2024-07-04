class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        output = []
        curr = 0
        for num in nums :
            curr = (2 * curr + num) % 5
            output.append(curr == 0)
        return output