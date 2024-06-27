class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        output = []

        for i in range(len(nums[0])) :
            output.append('0' if nums[i][i] == '1' else '1')
                

        return ''.join(output)