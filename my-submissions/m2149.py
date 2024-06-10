# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        outputIndex = 0

        pos, neg = 0, 0
        while outputIndex < len(nums) :
            while nums[pos] < 0 :
                pos += 1
            while nums[neg] > 0 :
                neg += 1
            
            output[outputIndex] = nums[pos]
            output[outputIndex + 1] = nums[neg]
            outputIndex += 2
            pos += 1
            neg += 1
        return output
            