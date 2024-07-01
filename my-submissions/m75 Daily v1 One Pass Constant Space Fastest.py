class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        indx, red = 0, len(nums) - 1

        while indx < red :
            while indx < red and nums[indx] == 0 :
                indx += 1
            while indx < red and nums[red] != 0 :
                red -= 1
            nums[indx], nums[red] = nums[red], nums[indx]

        white = len(nums) - 1
        while indx < white :
            while indx < white and nums[indx] == 1 :
                indx += 1
            while indx < white and nums[white] != 1 :
                white -= 1
            nums[indx], nums[white] = nums[white], nums[indx]