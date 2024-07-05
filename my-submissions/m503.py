class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        maxIndx = max(list(range(len(nums))), key=lambda x: nums[x])
        stk = [nums[maxIndx]]
        output = [0] * len(nums)
        
        for i in range(maxIndx - 1, maxIndx - 1 - len(nums), -1) :
            while stk and stk[-1] <= nums[i] :
                stk.pop()
            if stk :
                output[i] = stk[-1]
            else :
                output[i] = -1
            stk.append(nums[i])

        return output
