class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums.sort()

        while nums :
            curr = nums.pop()
            if not nums or nums[-1] != curr :
                return curr
            while nums and nums[-1] == curr :
                nums.pop()

        return -1
