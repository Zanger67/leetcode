class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = Counter(nums)
        indx = 0

        for _ in range(cnt.get(0, 0)) :
            nums[indx] = 0
            indx += 1
        for _ in range(cnt.get(1, 0)) :
            nums[indx] = 1
            indx += 1
        for _ in range(cnt.get(2, 0)) :
            nums[indx] = 2
            indx += 1